<template>
<div class="row col-md-9">
    <div class="col-md-9">
        <Loading v-show="show_load"/>
        <MD v-show="!show_load" :file_path="file_path" v-on:right_list_emit="right_list_emit"></MD>
    </div>
    <div v-show="!show_load" class="col-md-3">
        <div class="position-fixed right-list" :style="{height: fullHeight + 'px'}" v-for="group1 in right_list.c" :key="group1">
            <div v-for="group2 in group1.c" :key="group2">
                <div class="right-list-item" :class="{ 'selected-list' : group2.a}">
                    <router-link :to="'#'+group2.t"> {{ group2.n }} </router-link>
                </div>
                <div v-for="(group3, index) in group2.c" :key="group3">
                    <div class="right-list-item" :class="{ 'selected-list' : group3.a}">
                        <svg @click.stop="show[index]=!show[index]" :class="{ 'arrowTransform': !show[index], 'arrowTransformReturn': show[index]}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right-fill" viewBox="0 0 16 16">
                            <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                        </svg>
                        <router-link :to="'#'+group3.t"> <span class="place"/>{{ group3.n }}</router-link> 
                    </div>
                    <!-- <transition name="fade">-->
                    <div v-show="!show[index]">
                        <div v-for="group4 in group3.c" class="right-list-item" :class="{ 'selected-list' : group4.a}" :key="group4">
                            <router-link :to="'#'+group4.t"> <span class="place"/>{{ group4.n }} </router-link>
                        </div>
                    </div>
                    <!-- </transition> -->
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import MD from './MD.vue'
import Loading from './Loading.vue'

export default {
    name : 'Adetail',
    data() {
        return{
            result: null,
            file_path: "",
            right_list: [],
            anchor_list: [],
            show: [],
            dic: this.$route.params.dic,
            fullHeight: document.documentElement.clientHeight,
            show_load: true,
        }
    },
    components: {
        MD,
        Loading,
    },
    created() {
        this.dic = this.$route.path.split('/')[1]
        this.file_path = '/' + this.dic +'/'+this.$route.params.file[0]+'/'+this.$route.params.file[1]
    },
    mounted() {
        const that = this
        window.addEventListener('scroll',this.scrollHandle)
        console.log("fullHeight" + this.fullHeight)
        window.onresize = () => {
            return (() => {
                window.fullHeight = document.documentElement.clientHeight
                that.fullHeight = window.fullHeight
            })()
        }
    },
    watch : {
        $route () {
            if(this.$route.params.file !== undefined) {
                this.file_path = '/' + this.dic +'/'+this.$route.params.file[0]+'/'+this.$route.params.file[1]
            }
        },
        fullHeight (val) {
            if(!this.timer) {
                this.fullHeight = val
                this.timer = true
                let that = this
                setTimeout(function (){
                    that.timer = false
                },400)
            }
        },
    },
    methods: {
        right_list_emit(right_list) {
            this.right_list = right_list
            this.convertId2Anchor(this.right_list.c[0], 3)
            this.show_load = false
        },
        scrollHandle(e){
            let top = e.srcElement.scrollingElement.scrollTop;    // 获取页面滚动高度
            this.modifyBgcolor(top, this.right_list.c[0], 3)
        },
        convertRemToPixels(rem) {
            return rem * parseFloat(getComputedStyle(document.documentElement).fontSize);
        },
        /* goAnchor(selector) { */
        /*     let anchor = document.querySelector(selector) */
        /*     console.log(selector) */
        /*     console.log(anchor.offsetTop) */
        /*     document.documentElement.scrollTop = anchor.offsetTop - this.convertRemToPixels(5) */
        /* }, */
        modifyBgcolor(top, list, n) {
          if ( --n == 0) return
          for (let y in list.c){
              let item = list.c[y]
              let anchor = '#' + item.t
              if (document.querySelector(anchor) == undefined) {
                  continue
              }
              let item_top = document.querySelector(anchor).offsetTop - this.convertRemToPixels(5)
              let item2 = list.c[parseInt(y) + 1]
              let item2_top = 99999;
              if (item2 != undefined) {
                  let anchor2 = '#' + item2.t
                  if (document.querySelector(anchor2) == undefined) {
                      continue
                  }
                  item2_top = document.querySelector(anchor2).offsetTop - this.convertRemToPixels(5)
              }
              if (top >= item_top && top < item2_top) {
                  item.a = true
                  this.modifyBgcolor(top, list.c[y]);
              } else {
                  item.a = false
                  for (let z in list.c[y].c){
                      let item = list.c[y].c[z]
                      item.a = false
                  }
              }
          }
        },
        convertId2Anchor(list, n) {
            if ( --n == 0) return
            console.log("convertId2Anchor")
            console.log(this.right_list)
            for (let l1 in list.c) {
                console.log(list.c[l1])
                let tmp = list.c[l1].n.replace(/\s/g, '-').replace(/&/g, '').toLowerCase()
                let is_first = true
                while (this.anchor_list.includes(tmp)) {
                    if (is_first) {
                        tmp += '-1'
                        is_first = false
                    } else {
                        let num = tmp.split('-').pop()
                        num = parseInt(num, 10)+1
                        tmp = tmp.substring(0, tmp.lastIndexOf('-')) + '-' + num;
                    }
                }

                /* while (!this.anchor_list.values().includes(tmp)) { */
                /*     tmp += "1" */
                /* } */
                console.log(tmp)
                this.anchor_list.push(tmp)
                list.c[l1].t = tmp
                this.convertId2Anchor(list.c[l1])
            }
            console.log(this.anchor_list)
            /* id = id.replace(/\s/g, '-').replace(/&/g, '').toLowerCase() */
            /* console.log(id) */
            /* return id */
        },
    },
}
</script>

<style lang='scss'>
.right-list {
  overflow: auto;
}

.right-list-item {
  border-left-color: #75b1a9;
  border-left-width: 0.2rem;
  border-left-style: solid;
  padding-left: 1em;
  text-decoration:none;
  color: #757575;
  cursor: pointer;
}

.right-list-item a {
  text-decoration:none;
  color: #757575;
}

.selected-list {
  background-color: #75b1a9;
  color: #fff;
}

.selected-list a {
  color: #fff;
}

.right-list .place {
  margin-left:1rem;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.arrowTransform{
    transition: 0.3s;
    transform-origin: center;
    transform: rotateZ(90deg);
}
.arrowTransformReturn{
    transition: 0.3s;
    transform-origin: center;
    transform: rotateZ(0deg);
}
</style>

<template>
    <div class="col-md-7">
        <MD :file_path="file_path" v-on:right_list_emit="right_list_emit"></MD>
    </div>
    <div class="col-md-2">
        <div class="position-fixed right-list" :style="{height: fullHeight + 'px'}" v-for="group1 in right_list.c" :key="group1">
            <div v-for="group2 in group1.c" :key="group2">
                <router-link :to="'#'+group2.n.toLowerCase()" class="right-list-item" :class="{ 'selected-list' : group2.a}"> {{ group2.n }} </router-link>
                <div v-for="(group3, index) in group2.c" :key="group3">
                    <div class="right-list-item" :class="{ 'selected-list' : group3.a}">
                        <span @click="show[index]=!show[index]"> ^ </span>
                        <router-link :to="'#'+group3.n.toLowerCase()"> <span class="place"/>{{ group3.n }} </router-link> 
                    </div>
                    <!--<transition name="fade">-->
                    <div v-show="!show[index]">
                        <div v-for="group4 in group3.c" class="right-list-item" :class="{ 'selected-list' : group4.a}" :key="group4">
                            <router-link :to="'#'+group4.n.toLowerCase()"> <span class="place"/>{{ group4.n }} </router-link>
                        </div>
                    </div>
                    <!--</transition>-->
            </div>
        </div>
    </div>
    </div>
</template>

<script>
import MD from './MD.vue'
import 'highlight.js/scss/default.scss'
import 'highlight.js/styles/nord.css'
/* import bootstrap from 'bootstrap' */

export default {
    name : 'Adetail',
    data() {
        return{
            result: null,
            file_path: "",
            right_list: [],
            show: [],
            dic: this.$route.params.dic,
            fullHeight: document.documentElement.clientHeight,
        }
    },
    components: {
        MD,
    },
    created() {
        this.dic = this.$route.path.split('/')[1]
        this.file_path = '/' + this.dic +'/'+this.$route.params.file[0]+'/'+this.$route.params.file[1]+'.md'
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
                this.file_path = '/' + this.dic +'/'+this.$route.params.file[0]+'/'+this.$route.params.file[1]+'.md'
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
              let anchor = '#' + item.n
              if (document.querySelector(anchor) == undefined) {
                  continue
              }
              let item_top = document.querySelector(anchor).offsetTop - this.convertRemToPixels(5)
              let item2 = list.c[parseInt(y) + 1]
              let item2_top = 99999;
              if (item2 != undefined) {
                  let anchor2 = '#' + item2.n
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
      
        }
    },
}
</script>

<style lang='scss'>
.right-list {
  overflow: auto;
}

.right-list-item {
  border-left-color: rgb(178, 172, 162);
  border-left-width: 0.3rem;
  border-left-style: solid;
  padding-left: 1em;
  text-decoration:none;
}

.right-list-item a {
  text-decoration:none;
}

.selected-list {
  background-color: rgb(178, 172, 162);
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
</style>

<template>
    <div v-show="!loading" class="col-md-9 row">
        <div class="col-md-9">
            <div class="item card" v-for="item in show_list" :key="item" @click="jump(item.path)">
                <div class="card-body row">
                    <div class="col-9">
                        <h4 class="card-title title"> {{item.title}} </h4>
                        <div class="mb-2 mt-1 card-subtitle text-muted">
                            <span class="date"> {{item.date}} &nbsp;</span>
                            <span class="author"> {{item.author}} &nbsp;</span>
                            <span class="tag" v-for="tag in item.tag" :key="tag">&lt;{{tag}}&gt;&nbsp;</span>
                        </div>
                        <p class="card-text summary"> {{item.summary}} </p>
                    </div>
                    <div class="pic col-3">
                        <img class="img-fluid" :src="'/' + dic +'/'+item.cover" v-if="item.cover"/>
                    </div>
                </div>
            </div>
        </div>
        <!--<div class="col-md-3 tag-list">
            <div :style="{height: fullHeight + 'px'}">
                <div class="position-fixed">
                    <span :class="{'selected-tag': click_tag_list.includes(item)}" @click="clickTag(item)" class="tag" v-for="item in tag_list" :key="item">{{item}} </span>
                </div>
            </div>
        </div>-->
    </div>
    <div v-show="loading" class="col-md-9 placeholder-glow" aria-hidden="true">
        <div class="col-md-9">
            <div class="item card" v-for="item in 5" :key="item">
                <div class="card-body row">
                    <div class="col-9">
                        <h4 class="placeholder card-title title col-7"></h4>
                        <p class="mb-2 mt-1 card-text">
                            <span class="placeholder col-2 me-1"></span>
                            <span class="placeholder col-1 me-2"></span>
                            <span class="placeholder col-1 me-1" v-for="tag in 2" :key="tag"></span>
                        </p>
                        <p class="card-text">
                            <span class="placeholder col-7 me-1"></span>
                            <span class="placeholder col-4 me-1"></span>
                            <span class="placeholder col-4 me-1"></span>
                            <span class="placeholder col-2 me-1"></span>
                            <span class="placeholder col-5 me-1"></span>
                            <span class="placeholder col-5 me-1"></span>
                        </p>
                    </div>
                    <div class="placeholder pic col-3">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

    export default {
        name: "Alist",
        data() {
            return {
                show_list: [],
                show_index: 30,
                current_list: [],
                total_list: [],
                dic: '',
                file_list: this.$route.params.list,
                tag_list: [],
                click_tag_list: [],
                loading : true,
            }
        },
        mounted() {
            this.dic = this.$route.path.split('/')[1]
            document.documentElement.scrollTop = 0;
            this.reloadList()
            var that=this
            this.$nextTick(() => {
                // this.initScroll()
                window.onscroll = function() {
                    let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
                    let windowHeight = document.documentElement.clientHeight || document.body.clientHeight;
                    let scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
                    if(scrollTop + windowHeight >= scrollHeight - 300){
                        that.show_list = that.show_list.concat(that.current_list.slice(that.show_index, that.show_index + 20))
                        that.show_index += 20
                    }
                }
            })
        },
        watch: {
            $route () {
                document.documentElement.scrollTop = 0;
                let tmpdic = this.$route.path.split('/')[1]
                if (tmpdic == "note" || tmpdic == "article") {
                    this.dic = tmpdic
                    this.reloadList()
                }
            },
            /* total_list() { */
            /*     this.show_index = 30 */
            /*     this.current_list = this.total_list */
            /*     this.show_list = this.current_list.slice(0, this.show_index) */
            /* } */
        },
        methods: {
            jump (path) {
                this.$router.push({path: `/${this.dic}/detail/${path}`,})
            },
            reloadList() {
                this.loading = true
                let list = this.$route.params.list
                if(list == undefined) {
                    console.warn("reloadlist list is undefined")
                    return
                }
                var that=this
                let list_file = '/' + this.dic + '/list.json'
                axios.get(list_file).then((res) => {
                    if(list == 'home') {
                        that.total_list = res.data['total']
                    } else {
                        that.total_list = res.data.list[list]
                    }
                    that.show_index = 30
                    that.current_list = that.total_list
                    that.show_list = that.current_list.slice(0, that.show_index)
                    that.loading = false
                })
            },
            reloadTagList() {
                for (let i in this.total_list) {
                    for (let j in this.total_list[i].tag)
                    this.tag_list.push(this.total_list[i].tag[j])
                }
            },
            clickTag(item) {
                this.click_tag_list.push(item)
            }

        }

    }
</script>

<style lang="scss" scoped>
.item {
    margin:1rem;
    border-radius:2.5rem;
    padding-left:1rem;
    padding-right:1rem;
    border-width:0;
    background-color:$color7;
}

.tag-list .tag {
    border-radius: 1rem;
    border-style: solid;
    border-width: 0.1rem;
    padding: 0.2rem;
    padding-left: 0.5rem;
    padding-right: 0.5rem;
    margin-right: 0.5rem;
}

.tag-list .selected-tag {
    background-color: red;
}

</style>

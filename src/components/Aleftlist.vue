<template>
    <div :class="'col-md-'+left_width">
        <div :style="{height: fullHeight + 'px'}">
            <div class="list-group position-fixed left-list" :style="{width: left_width / 15 * 100 + '%'}">
                <li class="list-group-item item" aria-current="true" @click="$emit('list_emit', 'home')"> HOME </li>
                <div v-for="(item, key) in total_list" :key="item">
                    <div>
                    <li class="list-group-item item" @click="$emit('list_emit', key)" aria-current="true">
                    <svg v-show="is_show_file" @click.stop="show[key]=!show[key]" :class="{ 'arrowTransform': show[key], 'arrowTransformReturn': !show[key]}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right-fill" viewBox="0 0 16 16">
                        <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                    </svg>
                    <span v-show="is_show_file" class="place"/>{{key}}
                    </li>
                    <li v-show="show[key] && is_show_file" class="list-group-item item" aria-current="true" :class="{ 'selected-list' : item.selected}" v-for="item in item" :key="item" @click="$emit('file_emit', item.path)">
                        <span class="place"/>{{item.title}}
                    </li>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Aleftlist",
        emits: ['file_emit', 'list_emit'],
        props: {
            is_show_file : {
                default: true,
            },
            left_width: {
                default: 3,
            },
        },
        data() {
            return {
                fullHeight: document.documentElement.clientHeight,
                total_list: "",
                dic: "",
                show: {},
            }
        },
        watch: {
            $route() {
                this.reload_list()
            },
        },
        mounted() {
            this.dic = this.$route.path.split("/")[1]
            /* const uslug = require('uslug') */
            /* const uslugify = s => uslug(s) */
            const that = this
            window.addEventListener('scroll',this.scrollHandle)
            console.log("fullHeight" + this.fullHeight)
            window.onresize = () => {
                return (() => {
                    window.fullHeight = document.documentElement.clientHeight
                    that.fullHeight = window.fullHeight
                })()
            }
            this.reload_list()
        },
        methods: {
            file_expand(key) {
                this.show[key] = true
                /* console.log("file_expand") */
            },
            reload_list() {
                let sub = this.$route.path.split('/')
                axios.get('/'+this.dic+'/list.json').then((res) => {
                    /* console.log('res data = ', res.data) */
                    this.total_list = res.data.list
                    /* console.log(sub) */
                    for (let x in this.total_list) {
                        /* console.log('x' + x) */
                        for (let y in this.total_list[x]) {
                            /* console.log('y' + y) */
                            this.total_list[x][y]['selected'] = false
                        }
                    }
                    if (sub[2] == 'detail') {
                        /* console.log(this.total_list) */
                        /* console.log('selected') */
                        /* console.log(this.total_list[sub[3]]) */
                        let sub_list = this.total_list[sub[3]]
                        for(let x in sub_list) {
                            if (sub_list[x]['title'] == sub[4].split('.')[0]) {
                                sub_list[x]['selected'] = true
                                this.show[sub[3]] = true
                                /* console.log('selected is true') */
                                /* console.log(this.total_list) */
                                break
                            }
                        }
                        /* this.total_list[sub[3]][sub[4].split('.')[0]]['selected'] = true */
                    }
                })

            }
        }
    }
</script>

<style scoped>

.left-list {
  overflow: auto;
  margin-left:2rem;
  border-radius:1rem;
}
.left-list .item {
  background-color:#f1fa8c;
  cursor: pointer;
}

.left-list .selected-list {
  background-color:red;
}

.place {
    margin-right: 1.5rem;
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

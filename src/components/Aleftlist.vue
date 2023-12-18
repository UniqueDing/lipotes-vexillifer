<template>
    <div :class="'col-md-'+left_width" class="d-none d-sm-block">
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

    <div class="d-block d-sm-none">
        <div class="position-fixed left-button">
            <svg data-bs-toggle="offcanvas" data-bs-target="#offcanvasLeftlist" aria-controls="offcanvasLeftlist" xmlns="http://www.w3.org/2000/svg" width="32" height="64" fill="currentColor" class="bi bi-chevron-compact-right" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z"/>
            </svg>
        </div>
        <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasLeftlist" aria-labelledby="offcanvasLeftlistLabel">
            <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvasLeftlistLabel">{{$t('list')}}</h5>
                <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body">
                <div class="left-list">
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
                this.dic = this.$route.path.split("/")[1]
                this.reload_list()
            },
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
            this.dic = this.$route.path.split("/")[1]
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
                    this.total_list = res.data.list
                    for (let x in this.total_list) {
                        for (let y in this.total_list[x]) {
                            this.total_list[x][y]['selected'] = false
                        }
                    }
                    if (sub[2] == 'detail') {
                        let sub_list = this.total_list[sub[3]]
                        for(let x in sub_list) {
                            if (sub_list[x]['title'] == sub[4].split('.')[0]) {
                                sub_list[x]['selected'] = true
                                this.show[sub[3]] = true
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

<style lang="scss" scoped>

.left-list {
  overflow: auto;
  /* margin-left:2rem; */
  /* border-radius:1rem; */
}
.left-list .item {
  background-color:$color6;
  cursor: pointer;
}

.left-list .selected-list {
  background-color:$color10;
}

.place {
    margin-right: 1.5rem;
}

.arrowTransform {
    transition: 0.3s;
    transform-origin: center;
    transform: rotateZ(90deg);
}
.arrowTransformReturn {
    transition: 0.3s;
    transform-origin: center;
    transform: rotateZ(0deg);
}
.left-button {
    margin-top: 100%;
    margin-left: -1rem;
    border-radius: 0 0.5rem 0.5rem 0;
    z-index: 999;
    background-color:$color7;
}
</style>

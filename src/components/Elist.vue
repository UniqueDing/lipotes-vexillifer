<template>
    <div class="container-fluid col-md-10">
        <div class="row">
            <div class="col-md-2" v-for="item in show_list" :key="item">
                <div class="card" @click="jump(item.path)">
                    <img :src="item.cover" class="card-img-top" :alt="item.title">
                    <div class="card-body">
                        <h6 class="card-title">{{item.title}}</h6>
                        <hr/>
                        <div class="card-title meta">{{item.creator}}</div>
                        <div class="card-title meta">{{item.date}}</div>
                        <div class="card-title meta">{{item.publisher}}</div>
                        <p class="card-text content">{{item.description.substr(0,30)}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ePub from "epubjs"
import axios from 'axios'

export default {
    name: "Elist",
    data() {
        return {
            show_list: [],
            show_index: 20,
            current_list: [],
            total_list: [],
            dic: '',
            file_list: this.$route.params.list,
        }
    },
    mounted() {
        this.dic = this.$route.path.split('/')[1]
        var that=this
        this.$nextTick(() => {
            // this.initScroll()
            window.onscroll = function() {
                let scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
                let windowHeight = document.documentElement.clientHeight || document.body.clientHeight;
                let scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
                if(scrollTop + windowHeight >= scrollHeight - 300){
                    let temp = that.current_list.slice(that.show_index, that.show_index + 20)
                    that.show_list = that.show_list.concat(temp)
                    console.log('temp ' + temp)
                    temp.forEach(function(item) {
                        that.getCover(item)
                    })
                    that.show_index += 20
                }
            }
        })
        if (this.$route.params.list == '') {
            this.$router.push({path: `/ebook/home`,})
        } else {
            this.reloadList()
        }
    },
    watch: {
        $route () {
            if (this.$route.params.list == '') {
                this.$router.push({path: `/ebook/home`,})
            } else {
                this.reloadList()
            }
        },
    },
    methods: {
        jump (path) {
            this.$router.push({path: `/ebook/detail/${path}`,})
        },
        reloadList() {
            var that=this
            document.documentElement.scrollTop = 0;
            axios.get('/'+that.dic+'/list.json').then((res) => {
                console.log('res data = ', res.data)
                console.log(that.$route.params)
                let list = that.$route.params.list
                if(list == 'home' || list == '') {
                    that.total_list = res.data['total']
                } else {
                    that.total_list = res.data.list[list]
                }
                that.show_index = 20
                that.current_list = that.total_list
                that.show_list = that.current_list.slice(0, that.show_index)
                console.log('show_list = ', that.show_list)
                that.show_list.forEach(function(item) {
                    that.getCover(item)
                })
            })
        },
        getCover(item) {
            var book = ePub(item.path)
            item.cover = require('../assets/book.png')
            console.log('getcover' + item.path)
            book.coverUrl().then( function(cover) {
                console.log(cover)
                item.cover = cover
            })
        },
    }

}
</script>

<style scoped>
.card {
    margin: 0.4rem;
    border-radius: 1rem;
    height: 33rem;
}

.card hr {
    margin: 0.5rem;
}

.card .meta {
    margin: 0rem;
    padding: 0rem;
    font-size: 0.9rem;
}

.card .content {
    margin: 0rem;
    margin-top: 0.3rem;
    padding: 0rem;
    font-size: 0.8rem;
}
</style>

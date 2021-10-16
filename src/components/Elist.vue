<template>
    <div class="col-md-9">
        <div class="row">
            <div class="card" style="width: 18rem;" v-for="item in show_list" :key="item">
                <img :src="item.cover" class="card-img-top" :alt="item.title">
                <div class="card-body">
                    <h5 class="card-title">{{item.title}}</h5>
                    <h6 class="card-title">{{item.creator}}</h6>
                    <h6 class="card-text">{{item.date}} {{item.publisher}}</h6>
                    <p class="card-text">{{item.description.substr(0,60)}}</p>
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
            show_index: 30,
            current_list: [],
            total_list: [],
            dic: '',
            file_list: this.$route.params.list,
            env: '',
        }
    },
    mounted() {
        this.dic = this.$route.path.split('/')[1]
        this.env = this.$route.path.substr(0, this.$route.path.lastIndexOf('/'))
        console.log("env" + this.env)
        this.env = this.env.substr(0, this.env.lastIndexOf('/'))
        console.log("env" + this.env)
        this.reloadList()
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
    },
    watch: {
        $route () {
            this.reloadList()
        },
        /* total_list() { */
        /*     this.show_index = 30 */
        /*     this.current_list = this.total_list */
        /*     this.show_list = this.current_list.slice(0, this.show_index) */
        /* } */
    },
    methods: {
        jump (path) {
            this.$router.push({path: `/ebook/detail/${path}`,})
        },
        reloadList() {
            var that=this
            axios.get('/'+that.dic+'/list.json').then((res) => {
                console.log('res data = ', res.data)
                console.log(that.$route.params)
                if(that.$router.params == undefined) {
                    that.total_list = res.data['total']
                } else {
                    console.log(that.file_list)
                    that.total_list = res.data[that.file_list]
                }
                that.show_index = 30
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
    margin: 1rem;
    border-radius: 1rem;
}
</style>

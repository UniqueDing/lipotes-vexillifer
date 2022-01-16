<template>
    <div class="col-md-7">
        <div class="item card" v-for="item in show_list" :key="item" @click="jump(item.path)">
            <div class="card-body row">
                <div class="col-8">
                    <h4 class="card-title title"> {{item.title}} </h4>
                    <div class="mb-2 mt-1 card-subtitle text-muted">
                        <span class="date"> {{item.date}} &nbsp;</span>
                        <span class="author"> {{item.author}} &nbsp;</span>
                        <span class="tag" v-for="tag in item.tag" :key="tag">&lt;{{tag}}&gt;&nbsp;</span>
                    </div>
                    <p class="card-text summary"> {{item.summary}} </p>
                </div>
                <div class="pic col-4">
                <img class="img-fluid" :src="env +'/'+item.cover" v-if="item.cover"/></div>
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
                env: '',
            }
        },
        mounted() {
            this.dic = this.$route.path.split('/')[1]
            this.env = this.$route.path.substr(0, this.$route.path.lastIndexOf('/'))
            console.log("env" + this.env)
            this.env = this.env.substr(0, this.env.lastIndexOf('/'))
            console.log("env" + this.env)
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
                    this.reloadList()
                    this.dic = tmpdic
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
                let list = this.$route.params.list
                if(list == undefined) {
                    return
                }
                let loader = this.$loading.show()
                var that=this
                axios.get('/'+that.dic+'/list.json').then((res) => {
                    // console.log('res data = ', res.data)
                    // console.log(that.$route.params)
                    // console.log("list " + list)
                    if(list == 'home') {
                        that.total_list = res.data['total']
                    } else {
                        that.total_list = res.data.list[list]
                    }
                    that.show_index = 30
                    that.current_list = that.total_list
                    that.show_list = that.current_list.slice(0, that.show_index)

                    loader.hide();
                    /* console.log('show_list = ', that.show_list) */
                })
            }

        }

    }
</script>

<style scoped>
.item {
    margin:1rem;
    border-radius:2.5rem;
    padding-left:1rem;
    padding-right:1rem;
    border-width:0;
    background-color:#f8f8f2;
}

</style>

<template>
    <div class="col-md-7">
        <div class="item" v-for="item in show_list" :key="item" @click="jump(item.path)">
            <div> {{item.title}} </div>
            <div> {{item.data}} </div>
            <div> {{item.author}} </div>
            <div> {{item.tag}} </div>
            <div> {{item.summary}} </div>
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
            }
        },
        created() {
        },
        mounted() {
            axios.get('./note/listhome.json').then((res) => {
                console.log('res data = ', res.data)
                this.total_list = res.data.home
                this.current_list = res.data.home
                this.show_list = this.current_list.slice(0, this.show_index)
                console.log('show_list = ', this.show_list)
            })
            var that = this
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
            file_list () {
                console.log(this.file_list)
            },
        },
        methods: {
            jump (path) {
            this.$router.push({path: `/article/detail/${path}`,})
            }

        }

    }
</script>

<style scoped>
.item {
    border: 1px blue solid;
}
</style>

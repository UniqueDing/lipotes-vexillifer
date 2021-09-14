<template>
    <div class="col-md-3">
        <ul class="list-group position-fixed left-list" :style="{height: fullHeight + 'px'}">
            <li class="list-group-item item" aria-current="true" @click="$emit('list_emit', 'home')"> HOME </li>
            <div v-for="(item, key) in total_list" :key="item">
                <li class="list-group-item item" aria-current="true" @click="$emit('list_emit', key)"> {{key}} </li>
                <li class="list-group-item item" aria-current="true" v-for="item in item" :key="item" @click="$emit('file_emit', key +'/'+item.title)">
                    <span class="place"/>{{item.title}}
                </li>
            </div>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Aleftlist",
        emits: ['file_emit', 'list_emit'],
        data() {
            return {
                fullHeight: document.documentElement.clientHeight,
                total_list: "",
                dic: "",
            }
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
            axios.get('/'+this.dic+'/list.json').then((res) => {
                console.log('res data = ', res.data)
                let tmp = res.data.total
                delete tmp.home
                this.total_list = tmp
            })
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
}

.place {
    margin-right: 1.5rem;
}
</style>

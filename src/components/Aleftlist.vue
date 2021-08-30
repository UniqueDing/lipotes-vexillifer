<template>
    <div class="col-md-3">
        <ul class="list-group position-fixed leftlist">
            <li class="list-group-item" aria-current="true" @click="$emit('file_emit', 'home')"> HOME </li>
            <div v-for="(item, key) in total_list.total" :key="item">
                <li class="list-group-item" aria-current="true"> {{key}} </li>
                <li class="list-group-item" aria-current="true" v-for="item in item" :key="item" @click="$emit('file_emit', key +'/'+item.title)">
                    {{item.title}}
                </li>
            </div>
        </ul>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Aleftlist",
        emits: ['file_emit'],
        data() {
            return {
                total_list: "",
            }
        },
        mounted() {
            /* const uslug = require('uslug') */
            /* const uslugify = s => uslug(s) */
            /* var that = this */
            axios.get('./note/list.json').then((res) => {
                console.log('res data = ', res.data)
                this.total_list = res.data
            })
        }
    }
</script>

<style scoped>
</style>

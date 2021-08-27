<template>
    <div class="container">
        <div class="row">
            <Aleftlist></Aleftlist>
            <Alist v-on:file_path_click="show_detail" v-show="!is_show_detail"></Alist>
            <Ataglist v-show="!is_show_detail"></Ataglist>

            <Adetail v-show="!show" :file_path="file"></Adetail>
        </div>
    </div>
</template>

<script>
import Adetail from './Adetail.vue'
import Alist from './Alist.vue'
import Aleftlist from './Aleftlist.vue'
import Ataglist from './Ataglist.vue'

export default {
    name: "Article",
    data() {
        return {
            is_show_detail: false,
            file: ''
        }
    },
    components: {
        Adetail,
        Alist,
        Ataglist,
        Aleftlist,
    },
    methods: {
        show_detail(f) {
            this.file = f
            console.log(f)
            this.is_show_detail = true
        }
    },
}
</script>

<style scoped>
</style>

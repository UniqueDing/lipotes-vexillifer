<template>
    <div class="row">
        <Aleftlist v-on:file_emit="file_click"></Aleftlist>
        <router-view></router-view>
    </div>
</template>

<script>
/* import Adetail from './Adetail.vue' */
/* import Alist from './Alist.vue' */
import Aleftlist from './Aleftlist.vue'
/* import Ataglist from './Ataglist.vue' */

export default {
    name: "Article",
    data() {
        return {
            is_show_detail: false,
            file: ''
        }
    },
    components: {
        /* Adetail, */
        /* Alist, */
        /* Ataglist, */
        Aleftlist,
    },
    mounted() {
    },
    methods: {
        /* show_detail(f) { */
        /*     this.file = f */
        /*     console.log(f) */
        /*     this.is_show_detail = true */
        /* }, */
        file_click(file) {
            if (file == "home") {
                this.$router.push('/article')
                return
            }

            /* this.file = file */
            console.log("go  "+ file)
            this.$router.push({path: `/article/detail/${file}`,})
            /* this.is_show_detail = true */
        }
    },
}
</script>

<style scoped>
</style>

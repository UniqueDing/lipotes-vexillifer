<template>
    <div class="row">

        <Aleftlist class="d-none d-sm-block" v-on:file_emit="file_click" v-on:list_emit="list_click"></Aleftlist>
        <router-view></router-view>
    </div>
</template>

<script>
import Aleftlist from './Aleftlist.vue'

export default {
    name: "APage",
    data() {
        return {
            is_show_detail: false,
            file: '',
            dic: '',
            page: [
                'article',
                'note',
            ]
        }
    },
    components: {
        Aleftlist,
    },
    mounted() {
        this.dic = this.$route.path.split("/")[1]
        if(JSON.stringify(this.$route.params) === "{}") {
            this.$router.push({path: `/${this.dic}/list/home`})
        }
    },
    watch: {
        $route() {
            this.dic = this.$route.path.split("/")[1]
            console.log('dic ' + this.dic + " " + this.page.indexOf(this.dic))
            if(this.page.indexOf(this.dic) >= 0 && JSON.stringify(this.$route.params) === "{}") {
                this.$router.push({path: `/${this.dic}/list/home`})
            }
        }
    },
    methods: {
        file_click(file) {
            console.log("go  file "+ file)
            this.$router.push({path: `/${this.dic}/detail/${file}`})
        },
        list_click(list) {
            console.log("go  list "+ list)
            this.$router.push({path: `/${this.dic}/list/${list}`})
        }
    },
}
</script>

<style scoped>
</style>

<template>
    <div class="row">
        <Aleftlist v-on:file_emit="file_click" v-on:list_emit="list_click"></Aleftlist>
        <router-view></router-view>
    </div>
</template>

<script>
import Aleftlist from './Aleftlist.vue'

export default {
    name: "Article",
    data() {
        return {
            is_show_detail: false,
            file: '',
            dic: '',
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

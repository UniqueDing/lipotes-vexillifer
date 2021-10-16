<template>
    <div class="row">
        <Aleftlist :is_show_file=false v-on:list_emit="list_click"/>
        <Elist/>
    </div>
</template>

<script>
import Aleftlist from './Aleftlist.vue'
import Elist from './Elist.vue'

    export default {
        name: "Ebook",
        data() {
            return {
                dic: '',
                env: '',
                total_list: {},
                show_list: {},
                current_list: {},
            }
        },
        components: {
            Aleftlist,
            Elist,
        },
        mounted() {
            this.dic = this.$route.path.split('/')[1]
        },
        methods: {
            list_click(list) {
                console.log("go  list "+ list)
                this.$router.push({path: `/${this.dic}/${list}`})
            }
        },
    }
</script>

<style scoped>
</style>

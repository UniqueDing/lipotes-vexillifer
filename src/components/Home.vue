<template>
<div>
    <MD :file_path="file_path"></MD>
</div>
</template>

<script>
import MD from './MD.vue'
import axios from 'axios'

export default {
    name: "Home",
    data() {
        return {
            file_path:''
        }
    },
    components: {
        MD,
    },
    mounted() {
        var that = this
        axios.get('/article/list.json').then((res) => {
            that.file_path = 'article/' + res.data.web.home
        })
    }
}
</script>

<style scoped>
</style>

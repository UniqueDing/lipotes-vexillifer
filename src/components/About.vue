<template>
<div>
    <MD :file_path="file_path"></MD>
</div>
</template>

<script>
import MD from './MD.vue'
import axios from 'axios'

export default {
    name: "About",
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
            that.file_path = 'article/' + res.data.web.about
        })
    }
}
</script>

<style lang="scss" scoped>
</style>

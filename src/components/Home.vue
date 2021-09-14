<template>
    <div class="container">
        <MD :file_path="file_path"></MD>
    </div>
</template>

<script>
import MD from "./MD"

export default {
    name : 'App',
    data() {
        return{
            // TODO read from file
            file_path: "/article/test/markdown.md"
        }
    },
    components: {
        MD,
    },
}
</script>

<style lang='scss'>
</style>

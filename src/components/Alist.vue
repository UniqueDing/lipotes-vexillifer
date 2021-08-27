<template>
    <div class="col-md-7">
        <button class="btn" @click="$emit('file_path_click', './note/markdown/markdown.md')">btn</button>
    </div>
</template>

<script>

    export default {
        name: "Alist",
        emits: ['file_path_click']
    }
</script>

<style scoped>
</style>

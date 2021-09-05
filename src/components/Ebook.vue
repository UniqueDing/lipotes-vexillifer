<template>
    <div class="container">
        <div id="viewer"></div>
    </div>
</template>

<script>
import ePub from "epubjs"

    export default {
        name: "Ebook",
        mounted() {
            var book = ePub("./test.epub");
            var rendition = book.renderTo("viewer", {
              flow : "scrolled-doc",
              width : "100%"
            });
            book.loaded.navigation.then(function(toc) {
                console.log(toc)
            });
            rendition.display();
        }
    }
</script>

<style scoped>
</style>

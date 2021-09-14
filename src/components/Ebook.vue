<template>
    <div class="container">
        <div>
            <button class="btn" @click="prev">prev</button>
            <button class="btn" @click="next">next</button>
        </div>
        <div class="row">
            <div class="col-md-9" id="viewer"></div>
            <div class="col-md-3">
                <div class="postion-fixed">
                    <div v-for="item in toc" :key="item" @click="clickToc(item.href)">{{item.label}}<br></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import ePub from "epubjs"

    export default {
        name: "Ebook",
        data() {
            return {
                rendition: '',
                toc: [],
            }
        },
        mounted() {
            let that = this
            var book = ePub("./test.epub");
            this.rendition = book.renderTo("viewer", {
                manager: "continuous",
                /* flow: "scrolled", */
                /* flow : "scrolled-doc", */
                methods: "default",
                width : "100%",
            })
            this.rendition.display();
            book.loaded.navigation.then(function(toc) {
                console.log(toc)
                /* that.toc = that.recursionHandle(toc.toc, [], 0).join('') */
                that.toc = that.recursionHandle(toc.toc, [], 0)
                console.log(that.toc)
            })
        },
        methods: {
            prev() {
                this.rendition.prev()
            },
            next() {
                this.rendition.next()
            },
            recursionHandle (toc, doc, i) {
                let that = this
                toc.forEach(function(chapter) {
                    /* doc.push('<li class="toc-itme" click="click_toc(\''+ chapter.href +'\')">'+ chapter.label +'</li>') */
                    doc.push({href: chapter.href, label: chapter.label})
                    if(chapter.subitems && chapter.subitems.length) {
                        i++
                        that.recursionHandle(chapter.subitems, doc, i)
                        i > 0 && i--
                    }
                })
                return doc
            },
            clickToc(url) {
                console.log(url)
                this.rendition.display(url)
            }

        },
    }
</script>

<style scoped>
</style>

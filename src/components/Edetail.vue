<template>
    <div class="container">
        <div class="row">
            <div class="col-md-1">
                <button class="btn position-fixed" @click="prev">prev</button>
            </div>
            <div class="col-md-8" id="viewer"></div>
            <div class="col-md-2">
                <div class="position-fixed right-list">
                    <div v-for="item in toc" :key="item" @click="clickToc(item.href)">{{item.label}}<br></div>
                </div>
            </div>
            <div class="col-md-1">
                <button class="btn position-fixed" @click="next">next</button>
            </div>
        </div>
    </div>
</template>

<script>
import ePub from "epubjs"

    export default {
        name: "Edetail",
        data() {
            return {
                rendition: '',
                toc: [],
                cover: '',
                file_path: '',
            }
        },
        mounted() {
            this.getFilePath()
            this.open()
        },
        watch: {
            $route () {
                if (this.$route.path.split('/')[1] == 'ebook' && this.$route.path.split('/')[2] == 'detail' && this.$route.params.file !== undefined) {
                    document.documentElement.scrollTop = 0;
                    this.getFilePath()
                    this.open()
                }
            },
        },
        methods: {
            getFilePath() {
                this.file_path = '/ebook/' + this.$route.params.file[0] + '/' + this.$route.params.file[1]
            },
            open() {
                let that = this
                console.log(this.file_path)
                var book = ePub(this.file_path)
                console.log(book)
                this.rendition = book.renderTo("viewer", {
                    /* manager: "continuous", */
                    flow: "scrolled",
                    /* flow : "scrolled-doc", */
                    /* flow: "paginated", */
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
.right-list {
    color: #555;
}
</style>

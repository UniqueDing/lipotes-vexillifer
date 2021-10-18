<template>
    <div class="container">
        <div class="row">
            <div class="col-md-1">
                <div class="next position-fixed" @click="prev">
                    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-chevron-compact-left" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z"/>
                    </svg>
                </div>
            </div>
            <div class="col-md-8" id="viewer"></div>
            <div class="col-md-2">
                <div class="position-fixed right-list">
                    <div v-for="item in toc" :key="item" @click="clickToc(item.href)">{{item.label}}<br></div>
                </div>
            </div>
            <div class="col-md-1">
                <div class="next position-fixed" @click="next">
                    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-chevron-compact-right" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z"/>
                    </svg>
                </div>
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

.next {
    margin-top:25%;
    color: #aaa;
    cursor: pointer;
}
</style>

<template>
    <div class="container">
        <div v-show="!show_load" class="row">
            <div class="col-md-1">
                <div class="next position-fixed" @click="prev">
                    <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" fill="currentColor" class="bi bi-chevron-compact-left" viewBox="0 0 16 16">
                        <path fill-rule="evenodd" d="M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z"/>
                    </svg>
                </div>
            </div>
            <div class="col-md-8" id="viewer">
            </div>
            <div class="col-md-2">
                <div class="position-fixed right-list" :style="{height: fullHeight + 'px'}">
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
/* import InlineView from 'epubjs/lib/managers/views/inline' */

    export default {
        name: "Edetail",
        data() {
            return {
                rendition: '',
                toc: [],
                cover: '',
                file_path: '',
                fullHeight: document.documentElement.clientHeight,
                book: '',
                last_url: '',
            }
        },
        mounted() {
            var that = this
            window.addEventListener('scroll',this.scrollHandle)
            window.onresize = () => {
                return (() => {
                    window.fullHeight = document.documentElement.clientHeight
                    that.fullHeight = window.fullHeight
                })()
            }
            this.getFilePath()
            this.open()
        },
        watch: {
            $route () {
                if (this.$route.path.split('/')[1] == 'ebook' && this.$route.path.split('/')[2] == 'detail' && this.$route.params.file !== undefined) {
                    document.documentElement.scrollTop = 0
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
                let loader = this.$loading.show()
                let that = this
                /* console.log(this.file_path) */
                this.book = ePub(this.file_path)
                /* console.log(this.book) */
                this.rendition = this.book.renderTo("viewer", {
                    /* manager: "continuous", */
                    flow: "scrolled",
                    /* view: InlineView, */
                    /* flow : "scrolled-doc", */
                    /* flow: "paginated", */
                    methods: "default",
                    width : "100%",
                })
                this.rendition.display();
                this.book.loaded.navigation.then(function(toc) {
                    /* console.log(toc) */
                    /* that.toc = that.recursionHandle(toc.toc, [], 0).join('') */
                    that.toc = that.recursionHandle(toc.toc, [], 0)
                    loader.hide()
                    /* console.log(that.toc) */
                })

            },
            prev() {
                document.documentElement.scrollTop = 0
                this.rendition.prev()
            },
            next() {
                document.documentElement.scrollTop = 0
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
                this.rendition.display(url)
                /* console.log(url) */
                /* console.log(this.last_url) */
                /* let uu = url.split("#")[0] */
                /* if (uu !== this.last_url) { */
                /*     this.rendition.display(url.split("#")[0]) */
                /* } */
                /* if (url.split('#')[1]) { */
                /*     this.goAnchor('#' + url.split("#")[1]) */
                /* } */
                /* this.last_url = uu */
            },
            goAnchor(selector) {
                let anchor = document.querySelector(selector)
                console.log(selector)
                console.log(anchor.offsetTop)
                document.documentElement.scrollTop = anchor.offsetTop - this.convertRemToPixels(5)
            },
            convertRemToPixels(rem) {
                return rem * parseFloat(getComputedStyle(document.documentElement).fontSize);
            },
        },
    }
</script>

<style scoped>
.right-list {
    color: #555;
    overflow: auto;
    cursor: pointer;
}

.next {
    margin-top:20%;
    color: #aaa;
    cursor: pointer;
}

</style>

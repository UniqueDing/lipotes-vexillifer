<template>
          <div v-html="result" class="col-md-7"></div>
          <div class="col-md-2">
            <div class="position-fixed right-list" :style="{height: fullHeight + 'px'}" v-for="group1 in right.c" :key="group1">
                <div v-for="group2 in group1.c" :key="group2">
                    <div @click="goAnchor('#'+group2.n)" class="right-list-item" :class="{ 'selected-list' : group2.a}"> {{ group2.n }} </div>
                    <div v-for="(group3, index) in group2.c" :key="group3">
                        <div class="right-list-item" :class="{ 'selected-list' : group3.a}">
                        <span @click="show[index]=!show[index]"> ^ </span>
                        <span @click="goAnchor('#'+group3.n)"> {{ ' · '+ group3.n }} </span> 
                        </div>
                        <!--<transition name="fade">-->
                        <div v-show="!show[index]">
                            <div v-for="group4 in group3.c" class="right-list-item" :class="{ 'selected-list' : group4.a}" :key="group4">
                                <div @click="goAnchor('#'+group4.n)"> {{ ' · · '+ group4.n }} </div>
                            </div>
                        </div>
                        <!--</transition>-->
                    </div>
                </div>
            </div>
          </div>
</template>

<script>
import 'highlight.js/scss/default.scss'
import 'highlight.js/styles/nord.css'
import axios from 'axios'

export default {
    name : 'App',
    data() {
        return{
            result: null,
            file_path: "",
            right: [{l:0,n:0,c:null,a:false}],
            show: [],
            fullHeight: document.documentElement.clientHeight,
        }
    },
    components: {
    },
    created() {
            if(this.$route.params != '{}')
            this.file_path = this.$route.params.file[0]+'/'+this.$route.params.file[1]
        /* this.$watch( */
        /*   () => this.$route.params, */
        /*   (toParams, peParams) => { */
        /*     // 对路由变化做出响应... */
        /*     console.log(toParams) */
        /*     this.file_path = peParams.file[0]+'/'+peParams.file[1] */
        /*   } */
        /* ) */
    },
    mounted() {
        const that = this
        window.addEventListener('scroll',this.scrollHandle)
        console.log("fullHeight" + this.fullHeight)
        window.onresize = () => {
            return (() => {
                window.fullHeight = document.documentElement.clientHeight
                that.fullHeight = window.fullHeight
            })()
        }
    },
    watch : {
        $route () {
            console.log(this.$route.params)
            if(this.$route.params.file != undefined) {
                this.file_path = this.$route.params.file[0]+'/'+this.$route.params.file[1]
            }
            console.log(this.file_path)
        },
        fullHeight (val) {
            if(!this.timer) {
                this.fullHeight = val
                this.timer = true
                let that = this
                setTimeout(function (){
                    that.timer = false
                },400)
            }
        },
        file_path () {
            console.log("file_path" + this.file_path)
            const uslug = require('uslug')
            const uslugify = s => uslug(s)
            var that = this
            axios.get("./note/" + this.file_path + ".md").then((res) => {
                /* console.log('res data = ', res.data) */
                var hljs = require('highlight.js')
                var md = require('markdown-it')({
                    html: true,
                    linkify: true,
                    typographer: true,
                    highlight: function (str, lang) {
                    // 此处判断是否有添加代码语言
                    if (lang && hljs.getLanguage(lang)) {
                        try {
                            // 得到经过highlight.js之后的html代码
                            const preCode = hljs.highlight(str, {language:lang, ignoreIllegals:true}).value
                            // 以换行进行分割
                            const lines = preCode.split(/\n/).slice(0, -1)
                            // 添加自定义行号
                            let html = lines.map((item, index) => {
                              return '<li><span class="line-num" data-line="' + (index + 1) + '"></span>' + item + '</li>'
                            }).join('')
                            html = '<ol>' + html + '</ol>'
                            // 添加代码语言
                            if (lines.length) {
                              html += '<b class="name">' + lang + '</b>'
                            }
                            return '<pre class="hljs"><code>' + html + '</code></pre>'
                        } catch (e) {
                            console.log(e)
                        }
                    }
                    // 未添加代码语言，此处与上面同理
                    const preCode = md.utils.escapeHtml(str)
                    const lines = preCode.split(/\n/).slice(0, -1)
                    let html = lines.map((item, index) => {
                      return '<li><span class="line-num" data-line="' + (index + 1) + '"></span>' + item + '</li>'
                    }).join('')
                    html = '<ol>' + html + '</ol>'
                    return '<pre class="hljs"><code>' +
                      html +
                      '</code></pre>'
                    }
                })
                .use(require('markdown-it-plantuml'))
                .use(require('markdown-it-anchor').default, {
                    level: 1,
                    permalinkClass: 'header-anchor',
                    /* permalinkSymbol: '¶', */
                    permalinkSymbol: '%',
                    permalinkBefore: false,
                    slugify: uslugify
                })
                .use(require('markdown-it-toc-done-right').default, {
                    slugify: uslugify,
                    callback: function (html, ast) {
                    //把目录单独列出来
                        /* that.right = html */
                        console.log(html)
                        console.log(ast)
                        that.right = ast
                    }
                })

                this.result = md.render(res.data);
            })
        },
    },
    methods: {
      scrollHandle(e){
        let top = e.srcElement.scrollingElement.scrollTop;    // 获取页面滚动高度
        this.modifyBgcolor(top, this.right.c[0], 3)
      },
      convertRemToPixels(rem) {    
        return rem * parseFloat(getComputedStyle(document.documentElement).fontSize);
      },
      goAnchor(selector) {
          let anchor = document.querySelector(selector)
          console.log(selector)
          console.log(anchor.offsetTop)
          document.documentElement.scrollTop = anchor.offsetTop - this.convertRemToPixels(5)
      },
      modifyBgcolor(top, list, n) {
        if ( --n == 0) return
        for (let y in list.c){
            let item = list.c[y]
            let anchor = '#' + item.n
            let item_top = document.querySelector(anchor).offsetTop - this.convertRemToPixels(5)
            let item2 = list.c[parseInt(y) + 1]
            let item2_top = 99999;
            if (item2 != undefined) {
                let anchor2 = '#' + item2.n
                item2_top = document.querySelector(anchor2).offsetTop - this.convertRemToPixels(5)
            }
            if (top >= item_top && top < item2_top) {
                item.a = true
                this.modifyBgcolor(top, list.c[y]);
            } else {
                item.a = false
                for (let z in list.c[y].c){
                    let item = list.c[y].c[z]
                    item.a = false
                }
            }
        }

      }
    },
}
</script>

<style lang='scss'>
pre.hljs {
  padding: 8px 2px;
  border-radius: 5px;
  position: relative;
  ol {
    list-style: decimal;
    margin: 0;
    margin-left: 40px;
    padding: 0;
    li {
      list-style: decimal-leading-zero;
      position: relative;
      padding-left: 10px;
      .line-num {
        position: absolute;
        left: -40px;
        top: 0;
        width: 40px;
        height: 100%;
        border-right: 1px solid rgba(0, 0, 0, .66);
      }
    }
  }
  b.name {
    position: absolute;
    top: 2px;
    right: 12px;
    z-index: 10;
    color: #999;
    pointer-events: none;
  }
}

.right-list {
  overflow: auto;
}

.right-list-item {
  border-left-color: rgb(178, 172, 162);
  border-left-width: 4px;
  border-left-style: solid;
  padding-left: 1em;
}

.selected-list {
  background-color: rgb(178, 172, 162);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

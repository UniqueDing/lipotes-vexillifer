<template>
  <div class="container">
      <div class="row" style="margin-top:10rem;">
        <div class="col-md-2">A
            <router-link to="/about">about</router-link> 
        </div>
          <div v-html="result" class="col-md-8"></div>
          <div class="col-md-2">
            <div class="list-group position-fixed" v-for="group1 in right.c" :key="group1">
                <div class="list-group" v-for="group2 in group1.c" :key="group2">
                    <button type="button" @click="goAnchor('#'+group2.n)" :class="{ 'btn-primary' : group2.a}" class="btn btn-sm"> {{ group2.l + '. '+ group2.n }} </button>
                    <div class="list-group" v-for="(group3, index) in group2.c" :key="group3">
                        <li class="list-group-item list-group-item-action">
                        <button class="btn btn-sm" @click="show[index]=!show[index]">^</button>
                        <button @click="goAnchor('#'+group3.n)" class="btn btn-sm"> {{ group3.l + '. '+ group3.n }} </button> 
                        </li>
                        <!--<transition name="fade">-->
                        <i :class="{
                          'el-icon-arrow-down' : isCollapse,
                          'el-icon-arrow-up' : !isCollapse
                        }"></i>
                        <div v-show="!show[index]">
                        <div class="list-group" v-for="group4 in group3.c" :key="group4">
                            <button @click="goAnchor('#'+group4.n)" class="btn btn-sm list-group-item list-group-item-action"> {{ group4.l + '. '+ group4.n }} </button>
                        </div>
                        </div>
                        <!--</transition>-->
                    </div>
                </div>
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
            result : null,
            right : [{l:0,n:0,c:null,a:true}],
            show : [],
        }
    },
    components: {
    },
    created() {
        console.log(this.$router)
    },
    mounted() {
        window.addEventListener('scroll',this.scrollHandle);
        const uslug = require('uslug')
        const uslugify = s => uslug(s)
        var that = this
        axios.get('./note/markdown/markdown.md').then((res) => {
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
            }).use(require('markdown-it-plantuml')).use(require('markdown-it-anchor').default, {
                level: 1,
                permalinkClass: 'header-anchor',
                permalinkSymbol: '¶',
                permalinkBefore: false,
                slugify: uslugify
            }).use(require('markdown-it-toc-done-right').default, {
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
            /* console.log(this.result) */
            /* var result = md.render("# markdown-it rulezz!\n\n${toc}\n## with markdown-it-toc-done-right rulezz even more!"); */
            

            /* // browser without AMD, added to "window" on script load */
            /* // Note, there is no dash in "markdownit". */
            /* var md = window.markdownit({ */
            /*     html: false, */
            /*     xhtmlOut: true, */
            /*     typographer: true */
            /* }).use( window.markdownItAnchor, { permalink: true, permalinkBefore: true, permalinkSymbol: '§' } ) */
            /*   .use( window.markdownItTocDoneRight ); */

            /* var result = md.render("# markdown-it rulezz!\n\n${toc}\n## with markdown-it-toc-done-right rulezz even more!"); */
        })
    },
    methods: {
      scrollHandle(e){
        let top = e.srcElement.scrollingElement.scrollTop;    // 获取页面滚动高度
        /* console.log(top); */
        console.log(this.right.c[0].c)
        for (let x in this.right.c[0].c){
            let item = this.right.c[0].c[x]
            let anchor = '#' + item.n
            let item_top = this.$el.querySelector(anchor).offsetTop
            if (top > item_top) {
                item.a = false
            } else {
                item.a = true
            }
        }
      },
      goAnchor(selector) {
          var anchor = this.$el.querySelector(selector)
          console.log(selector)
          console.log(anchor.offsetTop)
          document.documentElement.scrollTop = anchor.offsetTop
      }
    },
    watch: {
      isCollapse(value) {
        if (!value) {
          this.$refs.List.style.overflow = "hidden"
          this.$refs.List.style.height = "30px"
        } else {
          this.$refs.List.style.overflow = "auto"
          this.$refs.List.style.height = "auto"
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>

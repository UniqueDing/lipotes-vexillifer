<template>
    <div>
        <div class="meta">
            <span>{{meta.author}} post:{{meta.date}}</span>
            <span class="item" v-for="item in meta.tag" :key="item">{{item}}</span>
        </div>
        <div v-html="result"></div>
    </div>
</template>

<script>
import 'highlight.js/scss/default.scss'
import 'highlight.js/styles/nord.css'
import axios from 'axios'

export default {
    name: 'MD',
    props: ['file_path'],
    emits: ['right_list_emit', 'meta_emit'],
    data() {
        return{
            result: null,
            meta: '',
        }
    },
    mounted() {
        console.log("file_path" + this.file_path)
        this.loadFile()
    },
    watch : {
        file_path () {
            this.loadFile()
        },
    },
    methods: {
        loadFile(){
            console.log("file_path" + this.file_path)
            const uslug = require('uslug')
            const uslugify = s => uslug(s)
            var that = this
            axios.get(this.file_path).then((res) => {
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
                        /* that.right = ast */
                        that.$emit("right_list_emit", ast)
                    }
                })
                .use(require('markdown-it-meta'))

                this.result = md.render(res.data)
                if (this.$route.hash != '') {
                    this.sleep(100).then(() => {
                        this.goAnchor(this.$route.hash)
                    })
                }
                this.meta = md.meta
                console.log(this.meta)

                let env = this.file_path.substr(0, this.file_path.lastIndexOf('/'))
                this.result = this.result.replace(/<img [^>]*src=['"]([^'"]+)[^>]*>/gi,function(match,capture){
                    let newStr='<img class="img-fluid" src="'+env+'/'+capture+'"/>'
                    return newStr
                })

            })

        },
        sleep (time) {
            return new Promise((resolve) => setTimeout(resolve, time));
        },
        goAnchor(selector) {
            let anchor = document.querySelector(selector)
            console.log(selector)
            console.log(anchor)
            console.log(anchor.offsetTop)
            document.documentElement.scrollTop = anchor.offsetTop - this.convertRemToPixels(5)
        },
        convertRemToPixels(rem) {
            return rem * parseFloat(getComputedStyle(document.documentElement).fontSize);
        },
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

.meta {
    padding-top:0.5rem;
    padding-bottom:0.5rem;
    color: #333;
}

.meta .item {
    padding:0.1rem;
    margin:0.2rem;
    border:0.1rem solid #aaa;
    border-radius:0.7rem;
}
</style>
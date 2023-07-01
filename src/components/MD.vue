<template>
    <div v-show="!loading">
        <div class="meta">
            <span>{{meta.author}} {{$t('create')}}:&nbsp; {{meta.date}} {{$t('update')}}:&nbsp; {{meta.modify}} tags: </span>
            <span class="item" v-for="item in meta.tag" :key="item">&nbsp;{{item}}</span>
            <hr/>
        </div>
        <div class="md" v-html="result"></div>
    </div>
    <div v-show="loading" class="card" aria-hidden="true">
        <div class="card-body">
            <h1 class="card-title placeholder-glow">
                <span class="placeholder col-6"></span>
            </h1>
            <div v-for="item in 10" :key="item">
                <h3 class="card-title placeholder-glow mt-3">
                    <span class="placeholder col-3"></span>
                </h3>
                <p class="card-text placeholder-glow">
                    <span class="placeholder col-5 me-2"></span>
                    <span class="placeholder col-6"></span>
                    <span class="placeholder col-7 me-2"></span>
                    <span class="placeholder col-4"></span>
                    <span class="placeholder col-9 me-1"></span>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
import 'highlight.js/styles/nord.css'
import dayjs from 'dayjs'
import axios from 'axios'

export default {
    name: 'MD',
    props: ['file_path'],
    emits: ['right_list_emit', 'meta_emit'],
    data() {
        return{
            result: null,
            meta: '',
            loading: true,
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
                .use(require('markdown-it-plantuml'), {
                    openMarker: '``` plantuml',
                    closeMarker: '```',
                    /* diagramName: 'ditaa', */
                    /* imageFormat: 'png' */
                })
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
                .use(require('markdown-it-footnote'))

                this.result = md.render(res.data)
                if (this.$route.hash != '') {
                    this.sleep(100).then(() => {
                        this.goAnchor(this.$route.hash)
                    })
                }
                this.meta = md.meta
                this.meta.date = dayjs(this.meta.date).format('YYYY-MM-DD')
                this.meta.modify = dayjs(this.meta.modify).format('YYYY-MM-DD')

                let env = this.file_path.substr(0, this.file_path.lastIndexOf('/'))
                this.result = this.result.replace(/<img [^>]*src=['"]([^'"]+)[^>]*>/gi,function(match,capture){
                    let newStr = ''
                    if (capture.slice(0,4) == 'http')
                        newStr='<img class="img-fluid" src="'+capture+'"/>'
                    else
                        newStr='<img class="img-fluid" src="'+env+'/'+capture+'"/>'
                    return newStr
                })

                this.loading = false
            })

        },
        sleep (time) {
            return new Promise((resolve) => setTimeout(resolve, time));
        },
        goAnchor(selector) {
            let anchor = document.querySelector(selector)
            document.documentElement.scrollTop = anchor.offsetTop - this.convertRemToPixels(5)
        },
        convertRemToPixels(rem) {
            return rem * parseFloat(getComputedStyle(document.documentElement).fontSize);
        },
    },
}
</script>

<style lang='scss'>
.meta {
    padding-top:0.5rem;
    padding-bottom:0.5rem;
    color: #333;
}

/* @import url('https://fonts.googleapis.com/css?family=Raleway:400,400i,500,500i,600,600i,700,700i'); */

.md {
    font-size: 16px;
    /* line-height: 1.6em; */
    -webkit-text-size-adjust: 100%;
    /* background-color: #fff; */
    /* color: #545454; */
    /* font-family: "Raleway", sans-serif; */
    /* font-family: "Hack"; */
    text-rendering: optimizeLegibility;
    /* max-width: 46em; */
    /* margin: 2em auto; */
    /* padding: 1.6em 3.15em; */
    /* line-height: 1; */

    ol,
    ul {
        list-style: none
    }

    table {
        border-collapse: collapse;
        border-spacing: 0
    }

    caption,
    th,
    td {
        text-align: left;
        font-weight: normal;
        vertical-align: middle
    }

    q,
    blockquote {
        quotes: none
    }

    q:before,
    q:after,
    blockquote:before,
    blockquote:after {
        content: "";
        content: none
    }

    a img {
        border: none
    }

    article, aside, details, figcaption, figure, footer, header, hgroup, main, menu, nav, section, summary {
        display: block
    }

    /* * { */
    /*     -moz-box-sizing: border-box; */
    /*     -webkit-box-sizing: border-box; */
    /*     box-sizing: border-box */
    /* } */


    h1 {
        /* font-family: "Raleway", sans-serif; */
        /* font-family: "Hack"; */
        font-weight: 700;
        color: $color1;
        font-size: 3rem;
        line-height: 5rem;
        margin-bottom: .78571rem
    }

    h2 {
        /* font-family: "Raleway", sans-serif; */
        font-weight: 600;
        color: $color1;
        font-size: 2rem;
        line-height: 3rem;
        margin-top: 2rem;
        margin-bottom: .6rem
    }

    h3 {
        /* font-family: "Raleway", sans-serif; */
        font-weight: 600;
        color: $color1;
        font-size: 1.5rem;
        line-height: 2rem;
        margin-top: 1rem;
        margin-bottom: .6rem
    }

    h4 {
        /* font-family: "Raleway", sans-serif; */
        font-weight: 500;
        color: $color1;
        font-size: 1.2rem;
        line-height: 1.5rem;
        margin-top: 1rem;
        margin-bottom: .6rem
    }

    p {
        margin-bottom: 1.57143em;
        hyphens: auto
    }


    b, strong {
        font-weight: 700;
    }

    i, em {
        font-style: italic;
    }

    u {
        text-decoration: none;
        background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0) 50%, $color12 50%);
        background-repeat: repeat-x;
        background-size: 2px 2px;
        background-position: 0 1.05em
    }

    s {
        color: $color8;
    }


    a {
        color: $color12;
        text-decoration: none
    }

    img {
        max-width: 100%;
        height: auto
    }

    blockquote {
        display: block;
        // margin-left: -1em;
        padding-left: 0.8em;
        border-left: 0.2em solid $color12;
        background-color: transparent;
    }

    hr {
        height: 1px;
        border: 0;
        background-color: $color5;
        margin: .7em auto .7em
    }

    /* LISTS */

    ul li:before {
        content: "•";
        color: $color12;
        display: inline-block;
        margin-right: 0.3em;
        font-size: 1.5em;
        vertical-align: middle;
    }


    ol{
        counter-reset: ol;
    }

    ol li {
        counter-increment: ol;
    }

    ol li:before {
        content: counter(ol) ".";
        color: $color13;
        text-align: right;
        display: inline-block;
        min-width: 1em;
        margin-right: 0.5em
    }


    /* TODO LIST */

    input[type="checkbox"] {
        position: relative;
        width: 1rem;
        height: 1rem;
        background: white;
        -webkit-appearance: none;
        border: 1px solid $color7;
        border-radius: .2em;
        margin: 0.2em .5em 0em -1.7em;
        margin-bottom: .5em;
        display: block;
        float: left;
        page-break-after: avoid;
    }

    input[type="checkbox"]:checked::before {
        display: block;
        content: '✓';
        display: initial;
        font-size: 1.1em;
        font-weight: bold;
        color: $color13;
        position: absolute;
        left: .1em;
        bottom: -0.2em;
    }

    input[type="checkbox"] ~ label {
        display: block;
        width: 100%;
        margin-bottom: 0.1em;
    }

    ul li input[type="checkbox"] {
        font: none;
    }

    ul li input[type="checkbox"] ~ label {
        display: inline-block;
        width: auto;
        margin-bottom: 0.1em;
        margin-left: 0.5em;
    }

    /*  TABLE */

    table {
        width: calc(100% + 3em);
        margin-bottom: 1.5em;
        margin-left: -1.5em;
    }

    table tr {
        border-bottom: 1px solid $color7;
    }

    table th {
        font-weight: 700;
    }

    table td, table th {
        vertical-align: top;
        padding: .2em 1.5em;
        font-size: .95em
    }

    thead tr {
        border-bottom: 4px double $color7;
    }
}

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
    li:before{
        display:none;
    }
  }
  b.name {
    position: absolute;
    top: 2px;
    right: 12px;
    z-index: 10;
    color: $color4;
    pointer-events: none;
  }
}

/* .meta .item { */
/*     padding:0.1rem; */
/*     margin:0.2rem; */
/*     border:0.1rem solid #aaa; */
/*     border-radius:0.7rem; */
/* } */
</style>

<template>
<nav :class="{trans: is_home}" class="navbar navbar-expand-sm navbar-light bg-light fixed-top">
    <a class="navbar-brand" href="/"> Lipotes Vexillifer </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
            <li class="nav-item" v-for="item in nav_items" :key="item">
                <router-link class="nav-link pl-4" :to="item[1]">{{$t(item[0])}}</router-link>
            </li>
        </ul>
        <ul class="ms-auto navbar-nav">
            <li class="nav-item">
                <div class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="search_message" @keyup.enter="search">
                    <!--<button class="btn btn-outline-success" type="submit">{{$t("search")}}</button>-->
                </div>
            </li>
            <li class="nav-item">
                <button class="btn" @click="clickZH"><img class="img-fluid language" src="../assets/language/Chinese.png" alt="zh"/></button>
                <button class="btn" @click="clickEN"><img class="img-fluid language" src="../assets/language/English.png" alt="en"/></button>
                <button class="btn" @click="clickJP"><img class="img-fluid language" src="../assets/language/Japanese.png" alt="jp"/></button>
            </li>
        </ul>
    </div>
</nav>
<div v-show="!is_home" class="nav-placeholder"></div>
</template>

<script>
export default{
    name : 'Navbar',
    data() {
        return {
            is_home: false,
            nav_items : [["home" , "/"],
                        ["article" , "/article/list/home"],
                        /* ["picture" , "/picture"], */
                        ["note" , "/note/list/home"],
                        // ["ebook" , "/ebook/home"],
                        ["about" , "/about"]],
            site: window.location.host,
            search_message: '',
        }
    },
    methods: {
        clickZH() {
            this.$i18n.locale = 'zh'
        },
        clickEN() {
            this.$i18n.locale = 'en'
        },
        clickJP() {
            this.$i18n.locale = 'jp'
        },
        search() {
            window.open('https://bing.com/search?q=site%3A' + this.site + '+' + this.search_message)
        }
    },
    watch: {
        $route () {
            if (this.$route.path === "/") {
                this.is_home = true
            } else {
                this.is_home = false
            }
        },
    },
}
</script>
<style scoped>
.nav-placeholder {
    position:relative;
    height:5rem;
    display:block;
}

.language {
    width:1.5rem;
    height:1rem;
    border-radius:0.2rem;
}

.trans {
    color:white !important;
    background-color:transparent !important;
}

.trans  a {
    color:white;
}

.trans a:hover {
    color:white;
}

.trans  .nav-link {
    color:white !important;
}
li {
    margin-left: 1rem;
}
</style>

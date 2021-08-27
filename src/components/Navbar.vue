<template>
<nav class="navbar navbar-expand-sm navbar-light bg-light fixed-top">
    <a class="navbar-brand" href="#">Blog</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse container-fluid" id="navbarNavDropdown">
        <ul class="navbar-nav">
            <li class="nav-item" v-for="item in nav_items" :key="item">
                <router-link class="nav-link" :to="item[1]">{{$t(item[0])}}</router-link>
            </li>
        </ul>
        <div class="d-flex navbar-nav">
            <li class="nav-item">
                <button class="btn" @click="clickZH">zh </button>
                <button class="btn" @click="clickEN">en </button>
                <button class="btn" @click="clickJP">jp </button>
            </li>
        </div>
    </div>
</nav>
</template>

<script>
export default{
    name : 'Navbar',
    data() {
        return {
            nav_items : [["home" , "/"], 
                        ["article" , "article"],
                        ["picture" , "picture"],
                        ["note" , "note"],
                        ["about" , "about"]],
        }
    },
    mounted() {
        console.log(this.$route.params.username)
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
    }
}
</script>
<style lang="scss" scoped>
</style>

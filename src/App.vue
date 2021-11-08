<template>
    <div class="global container-fluid">
        <Navbar></Navbar>
        <router-view></router-view>
    </div>
    <Footer></Footer>
</template>

<script>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

export default {
    name : 'App',
    components: {
        Navbar,
        Footer,
    },
}
</script>

<style scoped>
.container-fluid {
    padding-left: 0rem;
    padding-right: 0rem;
}
.global {
    min-height: 70rem;
    padding-left: 0rem;
    padding-right: 0rem;
}
</style>

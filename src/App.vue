<template>
    <Navbar></Navbar>
    <div class="global container-fluid">
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
.global {
    min-height: 70rem;
    font-family: 'Hack';
    /* padding-left: 0rem; */
    /* padding-right: 0rem; */
}
</style>

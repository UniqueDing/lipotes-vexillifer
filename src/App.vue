<template>
    <div class="container-fluid global">
        <Navbar></Navbar>
        <router-view></router-view>
        <Footer></Footer>
    </div>
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

<style lang='scss'>
</style>

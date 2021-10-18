<template>
    <div class="container-fluid global">
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

<style lang='scss'>
.global{
    min-height: 100rem;
}
</style>

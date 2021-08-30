<template>
    <div class="container-fluid global">
        <Navbar></Navbar>
        <router-view></router-view>
    </div>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
    name : 'App',
    components: {
      Navbar,
    },
}
</script>

<style lang='scss'>
.global {
    padding-top: 5rem;
}
</style>

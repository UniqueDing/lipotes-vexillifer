<template>
    <div class="container">
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
.container{
    margin-top:5rem;
}
</style>

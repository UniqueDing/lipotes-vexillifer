<template>
  <Navbar></Navbar>
  <!-- <HelloWorld></HelloWorld> -->
  <div v-html="result"></div>
</template>

<script>
import Navbar from './components/Navbar.vue'
/* import HelloWorld from './components/HelloWorld' */
import axios from 'axios'

export default {
  name : 'App',
  data() {
      return{
          result : null
      }
  },
  components: {
    /* HelloWorld, */
    Navbar,
    /* HelloI18n */
  },
  mounted() {
    axios.get('./note/markdown/markdown.md').then((res) => {
        /* console.log('res data = ', res.data) */
        var md = require('markdown-it')();
        this.result = md.render(res.data);
        console.log(this.result)
    })

  }
}
</script>

<style>

</style>

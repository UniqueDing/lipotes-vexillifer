<template>
<div>
  <nav>
    <scroll-spy
      :items="['#selection-1', '#selection-2', '#selection-3']"
      class="scroll-spy"
      tag="ul"
      current-class="active-class">
      <li><a href="#selection-1">One</a></li>
      <li><a href="#selection-2">Two</a></li>
      <li><a href="#selection-3">Three</a></li>
    </scroll-spy>
  </nav>
  <article style="font-size:5rem;">
    <section id="selection-1">{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}</section>
    <section id="selection-2">{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}</section>
    <section id="selection-3">{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}{{text}}</section>
  </article>
</div>
</template>

<script>

    export default {
        name: "about",
        data() {
            return {
                text: "rstrsainetttttttttttttttsfuywwwwwwwwwwwwwwwwwwvvvvkdhplyqdhw\n",
            }
        },
        created() {
        },
        mounted() {
        }
    }
</script>

<style scoped>
</style>

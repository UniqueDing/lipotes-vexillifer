<template>
<div>
    <div class="position-absolute top-50 start-50 translate-middle title">Lipotes Vexillifer</div>
    <canvas id="background"></canvas>
</div>
</template>

<script>

export default {
    name: "Home",
    data() {
    },
    mounted() {
        /* eslint-disable */
        WFSRun()
    }
}
</script>

<style scoped>
.title {
    z-index:10;
    color: white;
    font-size: 4rem;
    user-select: none;
    pointer-events: none;
}
#background {
    position: absolute;
    left: 0rem;
    width: 100%;
    height: 80rem;
}
</style>

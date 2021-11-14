<template>
    <footer class="footer">
        <div class="row row-cols-4">
            <div class="col" v-for="items in content" :key="items">
                <div>{{items.name}}</div>
                <div v-for="item in items.groups" :key="item">
                    <a :href="item.url">{{item.name}}</a>
                </div>
            </div>
        </div>
    </footer>
</template>

<script>
import axios from 'axios'
export default {
    name: "Footer",
    data() {
        return {
            content: [],
        }
    },
    mounted() {
        axios.get('/config/footer.json').then((res) => {
            console.log(res.data)
            this.content = res.data.content
        })
    },
}
</script>

<style scoped>
.footer {
    position: absolute;
    margin-top: 4rem;
    background-color: #000;
    width: 100%;
    padding: 3rem;
    color: #fff;
    z-index:9999;
}
.footer a {
    text-decoration:none;
    color: #bbb;
}
</style>

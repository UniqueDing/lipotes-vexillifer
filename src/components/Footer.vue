<template>
    <footer class="footer">
        <div class="row">
            <div class="col-md-3" v-for="items in content" :key="items">
                <h5>{{items.name}}</h5>
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
    background-color: #000;
    width: 100%;
    padding: 4rem;
    padding-left:10rem;
    color: #fff;
    z-index:9999;
}
.footer a {
    text-decoration:none;
    color: #bbb;
}
</style>

import './plugins/axios'
import { createApp } from 'vue'
import { createWebHistory, createRouter } from 'vue-router'
import App from './App.vue'
import Home from './components/Home.vue'
import Picture from './components/Picture.vue'
import APage from './components/APage.vue'
import About from './components/About.vue'
import Adetail from './components/Adetail.vue'
import Alist from './components/Alist.vue'
import Ebook from './components/Ebook.vue'
import Edetail from './components/Edetail.vue'

//bootstrap
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'

import i18n from './i18n'
import axios from './plugins/axios.js'

const scrollBehavior = function (to) {
    if (to.hash) {
        return {
            el: to.hash,
            behavior: 'smooth',
            top: 70,
        }
    }
}

const router = createRouter({
    history: createWebHistory(), // 路由模式
    scrollBehavior,
    base: '/',
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/home',
            component: Home
        },
        {
            path: '/picture',
            component: Picture
        },
        {
            path: '/article',
            component: APage,
            children: [
                {
                    path: 'list/:list',
                    component: Alist,
                },
                {
                    path: 'detail/:file+',
                    component: Adetail,
                },
            ]
        },
        {
            path: '/note',
            component: APage,
            children: [
                {
                    path: 'list/:list',
                    component: Alist,
                },
                {
                    path: 'detail/:file+',
                    component: Adetail,
                },
            ]
        },
        {
            path: '/ebook/:list?',
            component: Ebook
        },
        {
            path: '/ebook/detail/:file+',
            component: Edetail
        },
        {
            path: '/about',
            component: About
        },
    ]
})

const app = createApp(App)
    .use(i18n)
    .use(axios)
    .use(router)

app.mount('#app')

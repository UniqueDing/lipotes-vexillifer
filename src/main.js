import './plugins/axios'
import { createApp } from 'vue'
import { createWebHashHistory, createRouter } from 'vue-router'
import App from './App.vue'
import Home from './components/Home.vue'
import Picture from './components/Picture.vue'
import Article from './components/Article.vue'
import Note from './components/Note.vue'
import About from './components/About.vue'

//bootstrap
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import i18n from './i18n'
import axios from './plugins/axios.js'


const history = createWebHashHistory()
const router = createRouter({
  history, // 路由模式
  routes: [
    {
      path: '/',
      component: Home
    },
    {
      path: '/picture',
      component: Picture
    },
    {
      path: '/article',
      component: Article
    },
    {
      path: '/about',
      component: About
    },
    {
      path: '/note',
      component: Note
    }
  ]
})

createApp(App)
    .use(i18n)
    .use(axios)
    .use(router)
    .mount('#app')

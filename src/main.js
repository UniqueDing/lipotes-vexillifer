import './plugins/axios'
import { createApp } from 'vue'
import App from './App.vue'

//bootstrap
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import i18n from './i18n'
import axios from './plugins/axios.js'

createApp(App).use(i18n).use(axios).mount('#app')

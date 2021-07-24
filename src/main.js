import { createApp } from 'vue'
import App from './App.vue'

//bootstrap
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle.js'
import i18n from './i18n'

createApp(App).use(i18n).mount('#app')

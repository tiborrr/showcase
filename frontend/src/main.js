import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import './custom.scss';

axios.defaults.baseURL = process.env.VUE_APP_SHOWCASE_API_BASE_URL || process.env.VUE_APP_SHOWCASE_FALLBACK_API_BASE_URL
console.log(`baseURL: ${axios.defaults.baseURL}`)

const app = createApp(App)

app.use(router)
app.mount('#app')

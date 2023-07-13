/* Set up using Vue 3 */
import { createApp } from 'vue'
import App from './App.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faEdit, faTrash } from '@fortawesome/free-solid-svg-icons'

import router from './router'
import axios from 'axios'
import './custom.scss';

/* add icons to the library */
library.add(faEdit, faTrash)

axios.defaults.baseURL = process.env.VUE_APP_SHOWCASE_API_BASE_URL || process.env.VUE_APP_SHOWCASE_FALLBACK_API_BASE_URL
console.log(`baseURL: ${axios.defaults.baseURL}`)

createApp(App)
.component('font-awesome-icon', FontAwesomeIcon)
.use(router)
.mount('#app')

import { createRouter, createWebHashHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import Login from '../views/LoginPage.vue'

// A function to check if user is logged in
function isLoggedIn() {
  return localStorage.getItem('user_id') !== null;
}

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
    beforeEnter: (to, from, next) => {
      if (!isLoggedIn()) {
        next({ name: 'Login' });
      } else {
        next();
      }
    }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
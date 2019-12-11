import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../views/Login/Login.vue'
import Painel from '../views/Painel/Painel.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login
  },
  {
    path: '/painel',
    name: 'Painel',
    component: Painel
  },
]

const router = new VueRouter({
  routes
})

export default router

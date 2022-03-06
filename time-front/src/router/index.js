import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)
import Dashboard from '../views/Dashboard.vue'
import TimeTracker from '../views/TimeTracker.vue'
import Projects from '../views/Projects.vue'
import Account from '../views/Account.vue'
import PageNotFound from '../views/PageNotFound.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '*',
    name: 'PageNotFound',
    component: PageNotFound
  },
  {
    path: '/tracker',
    name: 'TimeTracker',
    component: TimeTracker
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects
  },
  {
    path: '/account',
    name: 'Account',
    component: Account
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
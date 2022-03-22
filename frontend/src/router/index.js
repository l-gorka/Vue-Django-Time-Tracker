import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '../store.js';

Vue.use(VueRouter);
import Home from '../views/Home.vue';

const isLoggedIn = (from, to, next) => {
  if (store.getters.loggedIn) {
    next();
  } else {
    store.commit('openLoginModal')
  }
};

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "Home" */'../views/Home.vue')
  },
  {
    path: '*',
    name: 'PageNotFound',    
    component: () => import(/* webpackChunkName: "NotFound" */'../views/PageNotFound.vue')
  },
  {
    path: '/tracker',
    name: 'TimeTracker',
    component: () => import(/* webpackChunkName: "Tracker" */'../views/TimeTracker.vue'),
    beforeEnter: isLoggedIn
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import(/* webpackChunkName: "Dashboard" */'../views/Dashboard.vue'),
    beforeEnter: isLoggedIn
  },
  {
    path: '/projects',
    name: 'Projects',
    component: () => import(/* webpackChunkName: "Project" */'../views/Projects.vue'),
    beforeEnter: isLoggedIn
  },
  {
    path: '/account',
    name: 'Account',
    component: () => import(/* webpackChunkName: "Account" */'../views/Account.vue'),
    beforeEnter: isLoggedIn
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
});

export default router;
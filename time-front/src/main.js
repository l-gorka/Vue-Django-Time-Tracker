import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Buefy from 'buefy'
import store from './store'
import 'buefy/dist/buefy.css'
import jwt_decode from "jwt-decode";


Vue.use(Buefy)
Vue.use(VueAxios, axios, store, jwt_decode)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

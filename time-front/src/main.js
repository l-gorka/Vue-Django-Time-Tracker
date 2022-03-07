import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Buefy from 'buefy'
import store from './store'
import 'buefy/dist/buefy.css'
import jwt_decode from "jwt-decode";
import VueLuxon from "vue-luxon";
import VueWait from 'vue-wait'


Vue.use(Buefy)
Vue.use(VueWait)
Vue.use(VueAxios, axios, store, jwt_decode, VueLuxon)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  wait: new VueWait({
    useVuex: true,
  }),
  render: h => h(App)
}).$mount('#app')

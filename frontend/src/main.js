import Vue from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import VueAxios from 'vue-axios';
import store from './store';
import 'buefy/dist/buefy.css';
import jwt_decode from "jwt-decode";
import VueWait from 'vue-wait';
import {
	Button, Navbar, Modal, Carousel, Field, Input, Loading, Dropdown,
	Icon, Tooltip, Toast, Notification, Datepicker, Collapse, Dialog, Pagination
} from 'buefy';


Vue.use(Button);
Vue.use(Navbar);
Vue.use(VueWait);
Vue.use(Modal);
Vue.use(Carousel);
Vue.use(Field);
Vue.use(Input);
Vue.use(Loading);
Vue.use(Dropdown);
Vue.use(Icon);
Vue.use(Tooltip);
Vue.use(Toast);
Vue.use(Notification);
Vue.use(Datepicker)
Vue.use(Collapse)
Vue.use(Dialog)
Vue.use(Pagination)
Vue.use(VueAxios, axios, store, jwt_decode);

Vue.config.productionTip = false;

new Vue({
	router,
	store,
	wait: new VueWait({
		useVuex: true,
	}),
	render: h => h(App)
}).$mount('#app');

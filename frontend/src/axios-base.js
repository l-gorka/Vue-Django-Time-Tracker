import axios from 'axios';
import jwtDecode from 'jwt-decode';
import store from './store';
//const APIUrl = 'http://127.0.0.1:8000';
const APIUrl = 'https://limitless-refuge-32819.herokuapp.com/';
import { SnackbarProgrammatic as snackbar } from "buefy";

const axiosBase = axios.create({
	baseURL: APIUrl,
	headers: { contentType: 'application/json' }
});
const getAPI = axios.create({
	baseURL: APIUrl
});
// get a new access token
getAPI.interceptors.request.use(async config => {
	let token = config.headers['Authorization'].split(' ')[1];
	token = jwtDecode(token).exp; // get expiration time from token
	if (Date.now() / 1000 > token - 10) {               // if the old token is about to expire
		let access = await store.dispatch('refreshToken'); // call refrehToken action
		config.headers.Authorization = `Bearer ${access}`; // set auth token and send original request
		return Promise.resolve(config);
	} else {
		return Promise.resolve(config);
	}
});
axiosBase.interceptors.response.use(
	// show snackbar if there is problem with connection
	response => response,
	(error) => {
		if (!error.response) {
			snackbar.open({
				duration: 6000,
				message: 'Problem connecting to the server.<br> Check internet connection and try again.',
				type: 'is-danger',
				position: 'is-bottom',
				actionText: 'ok',
			});

		} else {
			return Promise.reject(error)
		}
	}
);
export { axiosBase, getAPI };
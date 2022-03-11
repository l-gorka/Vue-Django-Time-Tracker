import Vue from 'vue';
import Vuex from 'vuex';
import jwtDecode from 'jwt-decode';
import { axiosBase, getAPI } from './axios-base';
import axios from 'axios'

Vue.use(Vuex);
export default new Vuex.Store({
	state: {
		accessToken: localStorage.getItem('access_token') || null, // makes sure the user is logged in even after
		// refreshing the page
		refreshToken: localStorage.getItem('refresh_token') || null,
		taskStarted: localStorage.getItem('task_started') || null,
		userID: localStorage.getItem('userID') || null,
		projects: [],
		timeEntries: [],
		dayEntries: [],
		continueTask: null,
		loginModalOpen: false
	},
	getters: {
		loggedIn(state) {
			return state.accessToken != null;
		},
		loginModalOpen(state) {
			return state.openLoginModal;
		}
	},
	mutations: {
		openLoginModal(state) {
			state.loginModalOpen = true;
		},
		closeLoginModal(state) {
			state.loginModalOpen = false;
		},
		updateProjects(state, projects) {
			state.projects = projects;
		},
		updateTimeEntries(state, timeEntries) {
			state.timeEntries = timeEntries;
		},
		updateDayEntries(state, dayEntries) {
			state.dayEntries = dayEntries
		},
		updateContinueTask(state, dataObj) {
			state.continueTask = dataObj;
		},
		deleteContinueTask(state) {
			state.continueTask = null;
		},
		// set cookie to preserve started task when reloading page
		updateTaskStarted(state, time) {
			localStorage.setItem('task_started', time);
			state.taskStarted = time;
		},
		deleteTaskStarted(state) {
			state.taskStarted = null;
		},
		updateLocalStorage(state, { access, refresh, userID }) {
			localStorage.setItem('access_token', access);
			localStorage.setItem('refresh_token', refresh);
			localStorage.setItem('userID', userID);
			state.accessToken = access;
			state.refreshToken = refresh;
			state.userID = userID;
		},
		updateAccess(state, access) {
			state.accessToken = access;
			localStorage.setItem('access_token', access);
		},
		destroyToken(state) {
			state.accessToken = null;
			state.refreshToken = null;
			state.userID = null;
		}
	},
	actions: {

		// remove current task cookie
		removeTaskStarted(context) {
			localStorage.removeItem('task_started');
			context.commit('deleteTaskStarted');
		},
		getProjects(context) {
			return new Promise((resolve, reject) => {
				getAPI.get("/project-list/", {
					headers: { Authorization: `Bearer ${context.state.accessToken}`, },
				}).then((response) => {
					context.commit('updateProjects', response.data);
					resolve(response.data.access);
				}).catch(err => {
					reject(err);
				});
			});
		},
		getTimeEntries1(context) {
			return new Promise((resolve, reject) => {
				getAPI.get("/time-entries/", {
					headers: { Authorization: `Bearer ${context.state.accessToken}`, },
				}).then((response) => {
					context.commit('updateTimeEntries', response.data);
					resolve(response.data.access);
				}).catch(err => {
					reject(err);
				});
			});
		},
		getTimeEntries1(context) {
			return new Promise((resolve, reject) => {
				axios.all([
					getAPI.get("/time-entries/", {
						headers: { Authorization: `Bearer ${context.state.accessToken}`, },
					}),
					getAPI.get("/project-list/", {
						headers: { Authorization: `Bearer ${context.state.accessToken}`, },
					}),
				]).then(axios.spread(function (timeEntriesResponse, projectsResponse) {
					
					context.commit('updateTimeEntries', timeEntriesResponse.data)
					context.commit('updateProjects', projectsResponse.data)
					resolve()
				})
				);
			});
		},
		getTimeEntries(context) {
			return new Promise((resolve, reject) => {
				axios.all([
					getAPI.get("/day-entries/", {
						headers: { Authorization: `Bearer ${context.state.accessToken}`, },
					}),
					getAPI.get("/time-entries/", {
						headers: { Authorization: `Bearer ${context.state.accessToken}`, },
					}),
					getAPI.get("/project-list/", {
						headers: { Authorization: `Bearer ${context.state.accessToken}`, },
					}),
				]).then(axios.spread(function (dayEntriesResponse, timeEntriesResponse, projectsResponse) {
					
					context.commit('updateTimeEntries', timeEntriesResponse.data)
					context.commit('updateDayEntries', dayEntriesResponse.data)
					context.commit('updateProjects', projectsResponse.data)
					resolve()
				})
				);
			});
		},
		// get a new access token on expiration
		refreshToken(context) {
			return new Promise((resolve, reject) => {
				axiosBase.post('/api/token/refresh/', {
					refresh: context.state.refreshToken
				}) // send the stored refresh token to the backend API
					.then(response => { // if API sends back new access and refresh token update the store
						context.commit('updateAccess', response.data.access);
						resolve(response.data.access);
					})
					.catch(err => {
						reject(err); // error generating new access and refresh token because refresh token has expired
					});
			});
		},
		registerUser(context, data) {

			return new Promise((resolve, reject) => {
				axiosBase.post('/register/', {
					email: data.email,
					username: data.username,
					password: data.password1,
				
				})
					.then(response => {
						resolve(response);
					})
					.catch(error => {
						reject(error);
					});
			});
		},
		logoutUser(context) {
			if (context.getters.loggedIn) {
				return new Promise((resolve, reject) => {
					axiosBase.post('/api/token/logout/')
						.then(response => {
							localStorage.removeItem('access_token');
							localStorage.removeItem('refresh_token');
							localStorage.removeItem('userID');
							context.commit('destroyToken');
						})
						.catch(err => {
							localStorage.removeItem('access_token');
							localStorage.removeItem('refresh_token');
							localStorage.removeItem('userID');
							context.commit('destroyToken');
							resolve(err);
						});
				});
			}
		},
		loginUser(context, credentials) {
			return new Promise((resolve, reject) => {
				// send the username and password to the backend API:
				axiosBase.post('/api/token/', {
					username: credentials.username,
					password: credentials.password
				})
					// if successful update local storage:
					.then(response => {
						let user = jwtDecode(response.data.access).user_id;

						context.commit('updateLocalStorage', { access: response.data.access, refresh: response.data.refresh, userID: user }); // store the access and refresh token in localstorage
						resolve();
					})
					.catch(err => {
						reject(err);
					});
			});
		}
	}
});
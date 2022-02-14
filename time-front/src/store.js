import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'
import { axiosBase } from './axios-base'

Vue.use(Vuex)
export default new Vuex.Store({
	state: {
		accessToken: localStorage.getItem('access_token') || null, // makes sure the user is logged in even after
		// refreshing the page
		refreshToken: localStorage.getItem('refresh_token') || null,
		taskStarted: localStorage.getItem('task_started') || null,
		userID: localStorage.getItem('userID') || null,
		APIData: '', // received data from the backend API is stored here.
		continueTask: null,
	},
	getters: {
		loggedIn(state) {
			return state.accessToken != null
		}
	},
	mutations: {
		updateContinueTask(state, dataObj) {
			state.continueTask = dataObj
			console.log(state.continueTask)
		},
		deleteContinueTask(state) {
			state.continueTask = null
		},
		// set cookie to prevent started task when reloading page
		updateTaskStarted(state, time) {
			localStorage.setItem('task_started', time)
			state.taskStarted = time
			console.log('store task str', state.taskStarted)
		},
		deleteTaskStarted(state) {
			state.taskStarted = null
		},
		updateLocalStorage(state, { access, refresh, userID }) {
			localStorage.setItem('access_token', access)
			localStorage.setItem('refresh_token', refresh)
			localStorage.setItem('userID', userID)
			state.accessToken = access
			state.refreshToken = refresh
			state.userID = userID
		},
		updateAccess(state, access) {
			state.accessToken = access
			localStorage.setItem('access_token', access)
		},
		destroyToken(state) {
			state.accessToken = null
			state.refreshToken = null
			state.userID = null
		}
	},
	actions: {
		
		// remove current task cookie
		removeTaskStarted(context) {
			localStorage.removeItem('task_started')
			context.commit('deleteTaskStarted')
		},
		// run the below action to get a new access token on expiration
		refreshToken(context) {
			return new Promise((resolve, reject) => {
				axiosBase.post('/api/token/refresh/', {
					refresh: context.state.refreshToken
				}) // send the stored refresh token to the backend API
					.then(response => { // if API sends back new access and refresh token update the store

						context.commit('updateAccess', response.data.access)
						resolve(response.data.access)
					})
					.catch(err => {

						reject(err) // error generating new access and refresh token because refresh token has expired
					})
			})
		},
		registerUser(context, data) {

			return new Promise((resolve, reject) => {
				axiosBase.post('/register/', {
					email: data.email,
					username: data.username,
					password1: data.password1,
					password2: data.password2
				})
					.then(response => {
						resolve(response)
					})
					.catch(error => {
						reject(error)
					})
			})
		},
		logoutUser(context) {
			if (context.getters.loggedIn) {
				return new Promise((resolve, reject) => {
					axiosBase.post('/api/token/logout/')
						.then(response => {
							localStorage.removeItem('access_token')
							localStorage.removeItem('refresh_token')
							localStorage.removeItem('userID')
							context.commit('destroyToken')
						})
						.catch(err => {
							localStorage.removeItem('access_token')
							localStorage.removeItem('refresh_token')
							localStorage.removeItem('userID')
							context.commit('destroyToken')
							resolve(err)
						})
				})
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
						let user = jwtDecode(response.data.access).user_id
						
						context.commit('updateLocalStorage', { access: response.data.access, refresh: response.data.refresh, userID: user}) // store the access and refresh token in localstorage
						resolve()
					})
					.catch(err => {
						reject(err)
					})
			})
		}
	}
})
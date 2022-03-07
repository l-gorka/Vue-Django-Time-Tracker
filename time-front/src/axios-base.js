import axios from 'axios'
import jwtDecode from 'jwt-decode'
import store from './store'
const APIUrl = 'http://127.0.0.1:8000'

const axiosBase = axios.create({
  baseURL: APIUrl,
  headers: { contentType: 'application/json' }
})
const getAPI = axios.create({
  baseURL: APIUrl
})
// get a new access token if the old is about to expire
getAPI.interceptors.request.use(async config => {
  let token = config.headers['Authorization'].split(' ')[1]
  token = jwtDecode(token).exp // get expiration time from token
  if (Date.now() / 1000 > token - 10) {
    let access = await store.dispatch('refreshToken')
    config.headers.Authorization = `Bearer ${access}`
    return Promise.resolve(config)    
  } else {
    return Promise.resolve(config)
  }
  
})

export { axiosBase, getAPI }
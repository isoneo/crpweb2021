//////        store/user/actions.js


import { axiosInstance } from 'boot/axios'
import JWT from 'jwt-client'

export function login ({ commit }, form) {
  console.log('action login')
  return axiosInstance.post('/login', { email: form.email, password: form.password })
    .then(response => {
      console.log('success login')
      let session = JWT.read(response.data.token)
      // console.log(response.data, session.claim.auth)
      commit('login', { token: response.data.token, refeshToken: response.data.refesh_token, user: response.data.user, authorization: session.claim.auth })
      setAxiosHeaders(response.data.token)
      return true
    })
    .catch((error) => {
      console.log('error login')
      // console.log(error.response.data)
      console.log(error)
      return false
    })
}

////////////   boot/axios.js
import axios from 'axios'
import { refreshToken } from '../store/user/getters';

const axiosInstance = axios.create({
  baseURL: 'https://0.0.0.0:5000'
   })
})

axiosInstance.interceptors.response.use((response) => { // intercept the global error
  return response
}, function (error) {
  let originalRequest = error.config
  if (error.response.status === 401 && !originalRequest._retry) { // if the error is 401 and hasent already been retried
    originalRequest._retry = true // now it can be retried 
    return axiosInstance.post('/users/token', null).then((data) => {
      return axiosInstance(originalRequest) // retry the request that errored out
    }).catch((error) => {
      for (let i = 0; i < error.response.data.errors.length; i++) {
        if (error.response.data.errors[i] === 'TOKEN-EXPIRED') {
          // refesh the token and try again
          refresh()
          return
        }
      }
    })
  }
  if (error.response.status === 404 && !originalRequest._retry) {
    originalRequest._retry = true
    window.location.href = '/'
    return
  }
  // Do something with response error
  return Promise.reject(error)
})

export default ({ Vue }) => {
  // for use inside Vue files through this.$axios
  Vue.prototype.$axios = axiosInstance
}

// Here we define a named export
// that we can later use inside .js files:
export { axiosInstance }

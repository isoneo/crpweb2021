//  axios boot example

import { boot } from 'quasar/wrappers'
import axios from 'axios'

const api = axios.create({ baseURL: 'https://api.example.com' })

export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
})

export { axios, api }


//  VUEX
import JWT from 'jwt-client'

export const logout = (state) => {
  // reset saved token
  state.token = null
  // remove token from local storage
  JWT.forget()
}

export const setToken = (state, { token, axios }) => {
  // all is good, validate the token
  if (JWT.validate(token)) {
    // keep token in localstorage
    JWT.keep(token)
    // update axios
    axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
    if (token) {
      axios.defaults.headers.common['X-Access-Token'] = token
    }
    else {
      axios.defaults.headers.common['X-Access-Token'] = ''
    }
    // console.log('token updated')
  }
  else {
    console.error('JWT failed to validate token')
    token = null
  }

  // console.log('old token:', state.token)
  state.token = token
  // console.log('new token:', state.token)

  return state.token
}


//////////////////////// router index
 function isValidLoggedIn () {
    let updatedToken = false
    let isLoggedIn = store.getters['auth/isLoggedIn']
    if (!isLoggedIn) {
      // see if there is a token in localstorage
      let token = JWT.get()
      if (token) {
        // check if expired
        if (tokenHelper.isExpired(token)) {
          console.error('Token expiredFor:', tokenHelper.expiredFor(token))
          token = null
        }
        else {
          updatedToken = true
        }
      }
      store.commit('auth/setToken', { token, axios: store.getters['http/axios'] })
      // re-get logged in status
      isLoggedIn = store.getters['auth/isLoggedIn']

      if (updatedToken && isLoggedIn) {
        store._vm.$emit('auth:logged-in')
      }
    }

    return isLoggedIn
  }


  //////////////////////////////// before each router
  let allowedToEnter = true
    to.matched.some((record) => {
      // check if there is meta data
      const isLoggedIn = isValidLoggedIn()
      if (!isLoggedIn && record.name === 'home') {
        next({
          path: '/sign-in',
          replace: true
        })
        return
      }

      if ('meta' in record) {
        // ------------------------------------------------------------
        // check if user needs to be logged in to access this page
        if ('requiresAuth' in record.meta) {
          if (record.meta.requiresAuth) {
            // console.log('Page requires auth:', to, from)
            // this route requires auth, check if user is logged in
            // if not, redirect to login page.
            if (!isLoggedIn) {
              // User is not logged in, redirect to signin page
              allowedToEnter = false
              next({
                path: '/sign-in',
                replace: true,
                // redirect back to original path when done signing in
                query: { redirect: to.fullPath }
              })
            }
          }
        }
        // ------------------------------------------------------------
        // check if user has correct permissions to access this page
        if (allowedToEnter && 'permissions' in record.meta) {
          let canProceed = false
          const permissions = record.meta.permissions
          // get currently logged in user permissions
          const token = store.getters['auth/token']
          // decipher the token
          const session = JWT.read(token)
          // check if they are not an admin (administrator)
          if (session.claim.permissions.administrator) {
            canProceed = true
          }
          else {
            for (let index = 0; index < permissions.length; ++index) {
              const permission = permissions[index]
              // console.log('Permission needed:', permission)
              if (permission === 'administrator') {
                if (session.claim.permissions.administrator) {
                  canProceed = true
                }
              }
              else if (permission === 'liveview') {
                if (session.claim.permissions.liveview) {
                  canProceed = true
                }
...
          if (!canProceed) {
            allowedToEnter = false
            // redirect to not-authorized page
            next({
              path: '/not-authorized',
              replace: true
            })
          }
        }
      }
    })

    if (allowedToEnter) {
      // go to the requested page
      next()
    }
  })
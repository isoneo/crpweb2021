import { userLogin, userLogout, userGetInfo, refreshJWT } from 'src/api/auth'
// import { loginByUsername, getUserInfo, refreshJWT } from 'src/api/auth'
// import { login, logout, getInfo } from '@/api/user'
import { checkLoggedIn, getToken, getAccessToken, getRefreshToken, setToken, removeToken, getToken_cookies } from 'src/utils/auth'
import router from 'src/router'
// import router, { resetRouter } from 'src/router'
// import * as Cookies from 'js-cookie'
import { Cookies, LocalStorage } from 'quasar'

const TokenKey = 'TOKEN_STORAGE_KEY'
const access_token = 'access'
const refresh_token = 'refresh'
const client_cookies = Cookies
const cookie_state = {
  // token: client_cookies.get('user-token') || '',
  token: getToken_cookies(),
  status: '',
  hasLoadedOnce: false
}

const state = {
  isLoggedIn: checkLoggedIn(),
  token: getToken(),
  token_access: getAccessToken(),
  token_refresh: getRefreshToken(),
  full_name: '',
  email: '',
  related_fund: [],
  related_department: [],
  setting: '',
  avatar: '',
  introduction: '',
  roles: [],
  user_cookies: cookie_state
}

const mutations = {
  SET_ISLOGGEDIN: (state, boolean) => {
    state.isLoggedIn = boolean
  },
  SET_TOKEN: (state, token) => {
    LocalStorage.set(TokenKey, token)
    LocalStorage.set(access_token, token[access_token])
    LocalStorage.set(refresh_token, token[refresh_token])
    state.token = token
  },
  SET_TOKEN_ACCESS: (state, token) => {
    LocalStorage.set(access_token, token)
    state.token_access = token
  },
  SET_TOKEN_REFRESH: (state, token) => {
    LocalStorage.set(refresh_token, token)
    state.token_refresh = token
  },
  SET_INTRODUCTION: (state, introduction) => {
    state.introduction = introduction
  },
  SET_NAME: (state, name) => {
    state.full_name = name
  },
  SET_EMAIL: (state, email) => {
    state.email = email
  },
  SET_RELATED_FUND: (state, related_fund) => {
    state.related_fund = related_fund
  },
  SET_RELATED_DEPARTMENT: (state, related_department) => {
    state.related_department = related_department
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  },
  SET_ROLES: (state, roles) => {
    state.roles = roles
  },
  SET_SETTINGS: (state, setting) => {
    state.setting = setting
  },
  SET_USERID: (state, userid) => {
    state.user_id = userid
  }
}

const actions = {
  // user login
  login({ commit,dispatch }, userInfo) {
    console.log('Attempting store user login')
    const username = userInfo.username.trim()
    const password = userInfo.password
    // console.log(username)
    return new Promise((resolve, reject) => {
      console.log(userInfo)
      userLogin(userInfo).then(response => {
        // console.log('Back to user')
        console.log(response)
        console.log(response.data[access_token])
        const data = response.data
        client_cookies.set('user-token', data[access_token])
        client_cookies.set('refresh-token', data[refresh_token])
        commit('SET_ISLOGGEDIN', true)
        commit('SET_TOKEN', data)
        commit('SET_TOKEN_ACCESS', data[access_token])
        commit('SET_TOKEN_REFRESH', data[refresh_token])
        setToken(data)
        // console.log('Set token worked')

        // console.log(getAccessToken())
        // console.log('Resolve worked')
        // dispatch('getInfo', data[access_token])  
        resolve()
        
      }).catch(error => {
        // console.log(err.status)
        console.log('failed attempted store user login')
        client_cookies.remove('user-token')
        reject(error)
      })
      // dispatch('getInfo')
      // .catch(error => {
      //   console.log(error)
      //   reject(error)
      // })
    })
    // dispatch('getInfo')
  },
  
  // get user info
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      // var usable_access_token
      // if (access_token_raw != null) {
      //   usable_access_token = access_token_raw
      // } else {
      //   usable_access_token = state.token_access
      // }
      userGetInfo().then(response => {
      // userGetInfo(state.token_access).then(response => {
        const data = response.data
        console.log("triggering getinfo")

        // if (!data) {
        //   reject('Verification failed, please Login again.')
        // }

        // const { roles, name, avatar, introduction } = data

        // // roles must be a non-empty array
        // if (!roles || roles.length <= 0) {
        //   reject('getInfo: roles must be a non-null array!')
        // }
        console.log(data)
        commit('SET_USERID', data.id)
        commit('SET_ROLES', 'admin')
        commit('SET_NAME', data.full_name)
        commit('SET_EMAIL', data.email)
        commit('SET_RELATED_FUND', data.related_fund)
        commit('SET_RELATED_DEPARTMENT', data.related_department)


        // commit('SET_NAME', name)
        // commit('SET_AVATAR', avatar)
        // commit('SET_INTRODUCTION', introduction)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state, dispatch }) {
    return new Promise((resolve, reject) => {
      // logout(state.token).then(() => {
      commit('SET_ISLOGGEDIN', false)
      commit('SET_TOKEN', '')
      commit('SET_TOKEN_ACCESS', '')
      commit('SET_TOKEN_REFRESH', '')
      commit('SET_ROLES', [])
      client_cookies.remove('user-token')
      removeToken()
      // resetRouter()

      // reset visited views and cached views
      // to fixed https://github.com/PanJiaChen/vue-element-admin/issues/2485
      // dispatch('tagsView/delAllViews', null, { root: true })

      resolve()
      // }).catch(error => {
      //   reject(error)
    })
    // })
  },
  refreshToken({ commit, state } ) {
    return new Promise((resolve, reject) => {
      console.log('Refresh Token area???')
      var refresh_data = {
        refresh:getRefreshToken()
      }
      refreshJWT(refresh_data).then(response => {
        // console.log(response)
        // console.log(response.data)
        // console.log('inside refresh token')
        const data = response.data
        client_cookies.set('user-token', data[access_token])
        commit('SET_TOKEN_ACCESS', data[access_token])
        // Cookies.set('user-token', data.token)
        // commit('SET_TOKEN_ACCESS', data.token)
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },
  // remove token
  resetToken({ commit }) {
    // return new Promise((resolve, reject) => {
    //   console.log('Reset Token area???')
    //   refreshJWT(state.token_refresh).then(response => {
    //     console.log(response)
    //     const data = response.data
    //     commit('SET_TOKEN_ACCESS', data.access)
    //   }).catch(error => {
    //     reject(error)
    //   })
    // })
    return new Promise(resolve => {
      console.log('Reset Token')
      client_cookies.remove('user-token')
      commit('SET_TOKEN', '')
      commit('SET_ROLES', [])
      removeToken()
      resolve()
    })
  },

  // dynamically modify permissions
  changeRoles({ commit, dispatch }, role) {
    return new Promise(async resolve => {
      // const token = role + '-token'

      // commit('SET_TOKEN', token)
      // setToken(token)

      // const { roles } = await dispatch('getInfo')
      // const roles = ['admin']
      const roles = 'admin'
      // resetRouter()

      // generate accessible routes map based on roles
      console.log('change roles generate routes')
      const accessRoutes = await dispatch('permission/generateRoutes', roles, { root: true })

      // dynamically add accessible routes
      router.addRoutes(accessRoutes)

      // reset visited views and cached views
      dispatch('tagsView/delAllViews', null, { root: true })

      resolve()
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

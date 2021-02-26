// import Cookies from 'js-cookie'
import { LocalStorage, Cookies } from 'quasar'

const TokenKey = 'TOKEN_STORAGE_KEY'
const access_token = 'access'
const refresh_token = 'refresh'

export function checkLoggedIn() {
  var selected_access_key;
  var log_check;
  
  try {
    selected_access_key = LocalStorage.getItem(access_token)
    console.log(localStorage)
  }
  catch(e) {
    console.error('error:', e, LocalStorage)
    console.log("Localstorage failed")
    selected_access_key = null
  }
  
  if (selected_access_key == null) {
    log_check = false
  } else {
    log_check = true
  }
  return log_check
}

export function getToken() {
  // return Cookies.get(TokenKey)
  
  var selected_token_key;
  try {
    selected_token_key = LocalStorage.getItem(TokenKey)  
  } 
  catch(err) {
    selected_token_key = ''
  }
  return selected_token_key  
}
export function getToken_cookies() {
  // return Cookies.get(TokenKey)
  
  var selected_token_key;
  try {
    selected_token_key = Cookies.get(TokenKey)  
  } 
  catch(err) {
    selected_token_key = ''
  }
  return selected_token_key  
}

export function getAccessToken() {
  // return Cookies.get(access_token)
  // console.log(LocalStorage.getItem(access_token))
  // if (typeof LocalStorage.getItem(access_token) === 'undefined') {
  //   return null
  // } else {
  //   return LocalStorage.getItem(access_token)
  // }
  var selected_access_key;
  try {
    selected_access_key = LocalStorage.getItem(access_token)
  }
  catch(err){
    console.log(err)
    selected_access_key = ''
  }
  return selected_access_key
  
}
export function getRefreshToken() {
  // return Cookies.get(refresh_token)
  var selected_refresh_key
  try {
    selected_refresh_key = LocalStorage.getItem(refresh_token)
  }
  catch(err) {
    console.log(err)
    selected_refresh_key=''
  }

  return selected_refresh_key
}
export function setToken(token) {
  // return Cookies.set(TokenKey, token)
  // Cookies.set(TokenKey, token)
  // Cookies.set(access_token, token.access)
  // Cookies.set(refresh_token, token.refresh)
  LocalStorage.set(TokenKey, token)
  LocalStorage.set(access_token, token[access_token])
  LocalStorage.set(refresh_token, token[refresh_token])

  return token
  // return Cookies.set(TokenKey, token)
}

export function removeToken() {
  // return Cookies.remove(TokenKey)
  LocalStorage.remove(TokenKey)
  return LocalStorage.clear()
}

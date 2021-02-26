// import service from 'src/utils/service'
// import { service } from 'src/boot/service.js'
import { service } from 'src/boot/axios.js'

export function userLogin(data) {
  return service({
    // url: '/login',
    url: '/auth/jwt/create/',
    method: 'post',
    data
  })
}

export function userGetInfo() {
  return service({
    url: '/user/custom_me',
    method: 'get',
    // params: { token }
  })
}

export function userLogout() {
  return service({
    url: '/user/logout',
    method: 'post'
  })
}

export function refreshJWT(refresh_data){
  return service({
    url: '/auth/jwt/refresh/',
    method: 'post',
    refresh_data
  })
}

export function userRegister(data) {
  return service({
    url: '/v1/users',
    method: 'post',
    data
  })
}

// List all users
export function userList(){
  return service({
    url: '/v1/users',
    method: 'get'
  })
}
// List specific User
export function userDetailInfo(id){
  return service({
    url: '/v1/users/' + id,
    method: 'get'
  })
}
// Update User Info
export function userPatchInfo(id, data){
  return service({
    url: '/v1/users/' + id,
    method: 'patch',
    data
  })
}
// Force Password Change
export function PWDForceUpdate(id, data){
  return service({
    url: '/v1/forcepassword/' + id,
    method: 'patch',
    data
  })
}
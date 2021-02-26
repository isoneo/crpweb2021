//  axios boot example

// import { boot } from 'quasar/wrappers'
// import axios from 'axios'

// const api = axios.create({ baseURL: 'https://api.example.com' })

// export default boot(({ app }) => {
//   // for use inside Vue files (Options API) through this.$axios and this.$api

//   app.config.globalProperties.$axios = axios
//   // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
//   //       so you won't necessarily have to import axios in each vue file

//   app.config.globalProperties.$api = api
//   // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
//   //       so you can easily perform requests against your app's API
// })

// export { axios, api };

import { boot } from "quasar/wrappers";
import axios from "axios";
// import { refreshToken } from "../store/user/getters";
import { getAccessToken } from "src/utils/auth";
// import { useStore } from 'vuex'
import { store_inst } from "../store"
const CSRF_COOKIE_NAME = "csrftoken";
const CSRF_HEADER_NAME = "X-CSRFToken";

axios.defaults.xsrfCookieName = CSRF_COOKIE_NAME;
axios.defaults.xsrfHeaderName = CSRF_HEADER_NAME;
// const store = useStore()
// Create Base Axios Service
const service = axios.create({
  // baseURL: 'https://0.0.0.0:5000'
  baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  // xsrfCookieName: CSRF_COOKIE_NAME,
  // xsrfHeaderName: CSRF_HEADER_NAME,
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 12000, // request timeout
});



// Add token info before sending request
service.interceptors.request.use(
  (config) => {
    // console.log('Service Request')
    console.log(config.url);
    console.log(store_inst)
    // console.log('test access token')
    // console.log(getAccessToken())
    // do something before request is sent
    console.log(process.env.VUE_APP_BASE_API);
    console.log("checking acceess token")
    console.log(getAccessToken())
    // console.log(getAccessToken());
    // console.log(store.getters);
    // console.log(store.getters.isLoggedIn);
    // console.log(store.getters.token);
    if (config.url != "/auth/jwt/create/") {
      try {
        if (getAccessToken()) {
          console.log("Trying Bearer Token "+getAccessToken())
          config.headers["Authorization"] = "Bearer " + getAccessToken();
          // console.log('Bearer ' + getAccessToken())
          config.headers["Content-Type"] = "application/json";
        }
      } catch (err) {
        console.log(err);
      }
    }

    // console.log(config)
    // console.log('Service Request finished')

    return config;
  },
  (error) => {
    // console.log('Service Request Error')
    // do something with request error

    // console.log(error) // for debug
    Promise.reject(error);
  }
);

// Check Axios Response
service.interceptors.response.use(
  (response) => {
    // intercept the global error
    return response;
  },
  function (error) {
    let originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      // if the error is 401 and hasnt already been retried
      originalRequest._retry = true; // now it can be retried
      return store_inst
        .dispatch('auth/refreshToken').then(() =>{
          return service(originalRequest); // retry the request that errored out
        })
        
        // .then((data) => {
        //   return service(originalRequest); // retry the request that errored out
        // })
        .catch((error) => {
          // for (let i = 0; i < error.response.data.errors.length; i++) {
          //   if (error.response.data.errors[i] === "TOKEN-EXPIRED") {
          //     // refesh the token and try again
          //     refresh();
          //     return;
          //   }
          // }
          console.log("Axios Refresh error")
        });
    }
    if (error.response.status === 404 && !originalRequest._retry) {
      originalRequest._retry = true;
      window.location.href = "/";
      return;
    }
    // Do something with response error
    return Promise.reject(error);
  }
);

// export default ({ Vue }) => {
//   // for use inside Vue files through this.$axios
//   Vue.prototype.$axios = service;
// };

export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = service;
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  // app.config.globalProperties.$api = api
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
});

// Here we define a named export
// that we can later use inside .js files:
export { service };

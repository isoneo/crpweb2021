import { store } from "quasar/wrappers";
import { createStore } from "vuex";
import getters from "./getters";
import auth from "./auth";
// import example from './module-example'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */
let store_inst = null
export default store(function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      auth,
      // example
    },

    getters,
    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    strict: process.env.DEBUGGING,
  });
  store_inst = Store
  return Store;
});

export { store_inst }
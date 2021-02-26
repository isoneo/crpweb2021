import Vue from 'vue'
import VueRouter from 'vue-router'

import routes from 'src/router'
import { boot } from 'quasar/wrappers'

export default boot(({ app, router, store, Vue }) => {

	console.log(store)
	// Router Guard
	// Protection from unauthenticated & role based
	router.beforeEach(( to, from, next ) => {	
	// Router Meta
	// - authenticationed : True / False
	// - allowedRole : [Multiple Role]
	// TODO: Add additional protection guards
	console.log(to)


	// Level 1 Protection - Authentication (change as neccessary)
	const authenticationed = to.meta.authenticationed
	const allowedRole = to.meta.allowedRole || true
	const userLogined = store.getters.isLoggedIn
	// const userRole = store.userRole
	const userRole = ""
	console.log(store.getters)
	console.log(userLogined)
	// If Authentication is not needed

	if (to.path==='/login') {
		return next()
	}
	if (authenticationed) {
		if (!userLogined) {
			console.log("Sending to Login Page")
			return next({
				path: '/login',
				query: {
					returnUrl: to.path
				}
			})
		}
		if (allowedRole) {
			// When Allowed Role meta exists and restricted
			if (userRole.length && !userRole.some(r=>allowedRole.includes(r))) {
				console.log("Role not allowed sending to dashboard")
				return next({path: '/'})
			} else {
				console.log("Ah okay sending to final page")
				next()
			}
		} else {
			// When No Role meta set and is not restricted
			console.log("NO Role check")
			next()
		}		
	} else {
		console.log("authentication not needed")
		next()
	}
	// else {
	// 	// When Authentication is needed
	// 	console.log("Sending to Login Page")
	// 		return next({
	// 			path: '/login',
	// 			query: {
	// 				returnUrl: to.path
	// 			}
	// 		})
	// }
	// next()

	})

})

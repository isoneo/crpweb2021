
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    
    children: [
      { path: '', component: () => import('pages/Index.vue'), meta: {authenticationed: true}, },
      
    ],
    
  },
  {
    path: '/user',
    component: () => import('layouts/MainLayout.vue'),
    meta: {authenticationed: true},
    children: [
      { path: 'profile', component: () => import('pages/auth/UserProfile.vue'),  },      
    ],
    
  },
  {
    path: '/src_ref',
    component: () => import('layouts/MainLayout.vue'),
    meta: {authenticationed: true},
    children: [
      { path: 'fund', component: () => import('pages/sources_reference/SrcFund.vue'),  },      
      { path: 'seller', component: () => import('pages/sources_reference/SrcSeller.vue'),  },      
    ],
    
  },

  {
    path: '/login',
    component: () => import('pages/auth/Login.vue'),
    // children: [
    //   { path: '', component: () => import('pages/auth/Login.vue') }
    // ]
  },
  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes

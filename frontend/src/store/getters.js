const getters = {
  // sidebar: state => state.app.sidebar,
  // size: state => state.app.size,
  // device: state => state.app.device,
  // visitedViews: state => state.tagsView.visitedViews,
  // cachedViews: state => state.tagsView.cachedViews,
  isLoggedIn: state => state.auth.isLoggedIn,
  setting: state => state.auth.setting,
  token: state => state.auth.token,
  token_access: state => state.auth.token_access,
  token_refresh: state => state.auth.token_refresh,
  avatar: state => state.auth.avatar,
  full_name: state => state.auth.full_name,
  email: state => state.auth.email,
  related_fund: state => state.auth.related_fund,
  related_department: state => state.auth.related_department,
  introduction: state => state.auth.introduction,
  roles: state => state.auth.roles,
  user_cookies: state => state.auth.user_cookies,
  // permission_routes: state => state.permission.routes,
  // errorLogs: state => state.errorLog.logs,
  // socket: state => state.websocket_st.socket,
  // socket_data: state => state.websocket_st.socket_data,
  // auto_fc: state => state.auto_fc.auto_fc_data
}
export default getters


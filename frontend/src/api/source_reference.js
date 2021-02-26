import { service } from 'src/boot/axios.js'

export function api_src_ref_fund_list(query) {
  return service({    
    url: '/src_ref/fund_list/',
    method: 'get',
    params: query
  })
}
export function api_src_ref_fund_add(data_info) {
  return service({    
    url: '/src_ref/fund_list/',
    method: 'post',
    data: data_info
  })
}

export function api_src_ref_seller_list(query) {
  return service({    
    url: '/src_ref/deal_seller/',
    method: 'get',
    params: query
  })
}
export function api_src_ref_seller_add(data_info) {
  return service({    
    url: '/src_ref/deal_seller/',
    method: 'post',
    data: data_info
  })
}

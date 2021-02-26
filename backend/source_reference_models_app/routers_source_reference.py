from rest_framework import routers
from .viewset_source_reference import *



router = routers.DefaultRouter()
router.register('deal_status', Src_tbl_deal_status_viewset)
router.register('deal_type', Src_tbl_deal_type_viewset)
router.register('deal_source', Src_tbl_deal_source_viewset)
router.register('deal_seller', Src_tbl_deal_seller_viewset)
router.register('afe_type', Src_afe_type_viewset)
router.register('department_list', Src_department_list_viewset)
router.register('fund_list', Src_fund_list_viewset)
router.register('int_type', Src_int_type_viewset)
router.register('payout_type', Src_payout_type_viewset)


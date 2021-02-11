from rest_framework import routers
from .viewset_custom_users import Gondor_mgmt_viewset



router = routers.DefaultRouter()
router.register('gondor_mgmt', Gondor_mgmt_viewset)
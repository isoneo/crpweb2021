from django.urls import path, include
from .routers_custom_user import router

from .custom_api import *

urlpatterns = [
    path('', include(router.urls)),
    path('custom_me', Gondor_mgmt_me_APIVIEW.as_view(), name='gondor_mgmt_me'),
    ]
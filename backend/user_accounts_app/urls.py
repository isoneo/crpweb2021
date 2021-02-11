from django.urls import path, include
from .routers_custom_user import router

urlpatterns = [
    path('', include(router.urls)),
    ]
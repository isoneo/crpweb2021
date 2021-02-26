from django.urls import path, include
from .routers_source_reference import router

urlpatterns = [
    path('', include(router.urls)),
    ]
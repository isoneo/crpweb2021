from rest_framework import  viewsets,pagination, response, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from utils.viewset_mixin import *

from .model_custom_user import Gondor_mgmt
from .serializers_custom_users import Gondor_mgmt_serializer



class Gondor_mgmt_viewset(viewsets.ModelViewSet):
    queryset = Gondor_mgmt.objects.all()
    serializer_class = Gondor_mgmt_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('related_user_fund','related_user_department',)
    search_fields = ()
    ordering_fields = '__all__'
    ordering = ()

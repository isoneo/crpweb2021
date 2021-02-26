from rest_framework import  viewsets,pagination, response, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from utils.viewset_mixin import *

from .model_sources import *
from .serializers_source_reference import *





class Src_tbl_deal_status_viewset(viewsets.ModelViewSet):
    queryset = Src_tbl_deal_status.objects.all()
    serializer_class = Src_tbl_deal_status_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('deal_status_code','deal_status_order','deal_status_text')
    search_fields = ('deal_status_code','deal_status_text')
    ordering_fields = '__all__'
    ordering = ('deal_status_order')


class Src_tbl_deal_type_viewset(viewsets.ModelViewSet):
    queryset = Src_tbl_deal_type.objects.all()
    serializer_class = Src_tbl_deal_type_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('deal_type', 'deal_type_helper')
    search_fields = ('deal_type',)
    ordering_fields = '__all__'
    # ordering = ('deal_status_order')


class Src_tbl_deal_source_viewset(viewsets.ModelViewSet):
    queryset = Src_tbl_deal_source.objects.all()
    serializer_class = Src_tbl_deal_source_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('deal_source', 'deal_source_helper')
    search_fields = ('deal_source', 'deal_source_helper')
    ordering_fields = '__all__'
    # ordering = ('deal_status_order')

class Src_tbl_deal_seller_viewset(viewsets.ModelViewSet):
    queryset = Src_tbl_deal_seller.objects.all()
    serializer_class = Src_tbl_deal_seller_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('seller_name', 'company','main_contact_person_name','main_email')
    search_fields = ('seller_name', 'company','main_contact_person_name','main_email',)
    ordering_fields = '__all__'

class Src_afe_type_viewset(viewsets.ModelViewSet):
    queryset = Src_afe_type.objects.all()
    serializer_class = Src_afe_type_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('afe_type', 'afe_type_descrip')
    search_fields = ('afe_type',)
    ordering_fields = '__all__'

class Src_department_list_viewset(viewsets.ModelViewSet):
    queryset = Src_department_list.objects.all()
    serializer_class = Src_department_list_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('dept_name', 'dept_name_descrip')
    search_fields = ('dept_name','dept_name_descrip')
    ordering_fields = '__all__'


class Src_fund_list_viewset(viewsets.ModelViewSet):
    queryset = Src_fund_list.objects.all()
    serializer_class = Src_fund_list_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('fund_name', 'fund_name_descrip')
    search_fields = ('fund_name', 'fund_name_descrip')
    ordering_fields = '__all__'


class Src_int_type_viewset(viewsets.ModelViewSet):
    queryset = Src_int_type.objects.all()
    serializer_class = Src_int_type_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('int_type_name', 'int_type_name_descrip')
    search_fields = ('int_type_name', 'int_type_name_descrip')
    ordering_fields = '__all__'


class Src_payout_type_viewset(viewsets.ModelViewSet):
    queryset = Src_payout_type.objects.all()
    serializer_class = Src_payout_type_serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPaginationAddPageQuery
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('payout_type', 'payout_type_descrip')
    search_fields = ('payout_type', 'payout_type_descrip')
    ordering_fields = '__all__'

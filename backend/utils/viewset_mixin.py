from rest_framework import  viewsets,pagination, response, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    # max_page_size = 100

    # Paginate in the style defined by vuetable2
    def get_paginated_response(self, data):

        # Get id's of records in current page
        firstRecord = data[0]['id'] if (data and 'id' in data[0]) else None
        lastRecord = data[-1]['id'] if (data and 'id' in data[0]) else None

        return response.Response({
            'pagination': {
                'total': self.page.paginator.count,
                'per_page': self.get_page_size(self.request),
                'current_page': self.request.query_params.get('page', None),
                'last_page': self.page.paginator.num_pages,
                'next_page_url': self.get_next_link(),
                'previous_page_url': self.get_previous_link(),
                'first': firstRecord,
                'last': lastRecord,
            },
            'data': data
        })

class CustomPaginationAddPageQuery(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
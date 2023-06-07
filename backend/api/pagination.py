from rest_framework.pagination import PageNumberPagination

from backend.settings import PAGE_SIZE


class Paginator(PageNumberPagination):
    page_size = PAGE_SIZE
    page_size_query_param = 'limit'

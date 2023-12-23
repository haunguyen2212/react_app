from rest_framework.pagination import PageNumberPagination, CursorPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class InfiniteScrollPagination(CursorPagination):
    page_size = 10
    ordering = 'id'
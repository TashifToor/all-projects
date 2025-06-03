from rest_framework.pagination import CursorPagination
class mycurserpanigation(CursorPagination):
    page_size=7
    ordering='name'
    cursor_query_param='cu'
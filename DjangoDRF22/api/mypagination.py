from rest_framework.pagination import PageNumberPagination
class Mypagenumberpagnition(PageNumberPagination):
    page_size=4
    page_query_param='p'
    page_size_query_param='records'#This allows clients to override the default page_size by including a query parameter.

#Example: ?p=1&records=10 would request page 1 with 10 items per page.
    max_page_size=7
    last_page_strings='end'#mean last similar name examole p=last by default
from rest_framework.pagination import LimitOffsetPagination

class mylimmitofferpagination(LimitOffsetPagination):
    default_limit=5#It sets the default number of items (results) that will be returned if the client does not specify a limit query parameter.
    limit_query_param='l'#?limit now not not work l will work
    offset_query_param='myoffset' #now ofset will no work
    max_limit=7
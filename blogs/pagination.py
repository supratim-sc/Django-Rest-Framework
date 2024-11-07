from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2

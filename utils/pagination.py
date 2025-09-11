from rest_framework.pagination import PageNumberPagination

from decouple import config

QUANTITY_ITEMS_PER_PAGE = config("QUANTITY_ITEMS_PER_PAGE")


class Pagination:
    @staticmethod
    def paginate(queryset, request, serializer_class):
        paginator = PageNumberPagination()
        paginator.page_size = QUANTITY_ITEMS_PER_PAGE
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = serializer_class(result_page, many=True)
        return paginator.get_paginated_response({"data": serializer.data})
from rest_framework.pagination import PageNumberPagination


class SnippetPage(PageNumberPagination):
    page_size = 3
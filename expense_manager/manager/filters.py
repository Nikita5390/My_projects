from rest_framework import filters
from datetime import datetime


class TransactionFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        count = dict(request.query_params).get('count')
        date = dict(request.query_params).get('date')
        organization = dict(request.query_params).get('organization')
        result = queryset.all()
        if count:
            result = result.filter(count__in=count)
        if date:
            result = result.filter(date__in=date)
        if organization:
            result = result.filter(organization__in=organization)
        return result


class CategoryFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        title = dict(request.query_params).get('title')
        result = queryset.all()
        if title:
            result = result.filter(title__in=title)
        return result

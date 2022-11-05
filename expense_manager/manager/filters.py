from rest_framework import filters


class TransactionFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        count = dict(request.query_params).get('count')
        date = dict(request.query_params).get('date')
        result = queryset.all()
        if count:
            result = result.filter(name__in=count)
        if date:
            result = result.filter(name__in=date)
        return result

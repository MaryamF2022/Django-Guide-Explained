from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from .models import Author

class DateListView(ArchiveIndexView):
    model = Author
    date_field = 'birth_date'
    allow_future = False
    allow_empty = True
    date_list_period = 'year'
    context_object_name = 'authors'
    template_name = 'authors.html'

    # def get_date_list(self, *args, **kwargs):
    #     qs = self.get_dated_queryset()
    #     return super().get_date_list(qs, ordering = 'ACS')

    def get_dated_queryset(self, **lookup: Any):
        
        
        queryset = super().get_dated_queryset(**lookup)
        queryset = queryset.order_by('birth_date')
        return queryset
    
    def get_dated_items(self):
        date_list, object_list, context = super().get_dated_items()
        date_list = sorted(date_list)
        return date_list, object_list, context
    # def get_dated_items(self):
    #     """Return (date_list, items, extra_context) for this request."""
    #     qs = self.get_dated_queryset()
    #     date_list = self.get_date_list(qs, ordering="DESC")

    #     if not date_list:
    #         qs = qs.none()

    #     return (date_list, qs, {})


class AuthorYearArchiveView(YearArchiveView):
    model = Author
    make_object_list = True
    date_field = 'birth_date'
    allow_future = False
    allow_empty = True
    template_name = 'author_year_archive.html'


class AuthorMonthArchiveView(MonthArchiveView):
    model=Author
    make_object_list = True
    date_field = 'birth_date'
    allow_future = False
    allow_empty = True
    template_name = 'author_month_archive.html'
    month_format = '%m'
from datetime import date
from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Book, Commentors, Author

def make_published(modeladmin, request, queryset):
    queryset.update(status = Book.BookStatus.PUBLISHED)

def make_unpublished(modeladmin, request, queryset):
    queryset.update(status = Book.BookStatus.UNPUBLISHED)

class DatePublishedFilter(admin.SimpleListFilter):
    title = 'Publishing Date'
    parameter_name = 'published'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        if qs.filter(
            date_published__gte = date(2000, 1, 1),
            date_published__lte = date(2010, 1, 1),
        ).exists():
            yield ('2000', 'Published recently in 2010')
        if qs.filter(
            date_published__gte = date(2010, 1, 1),
            date_published__lte = date(2020, 1, 1,),
        ).exists():
            yield ('2010', 'Published recently in 2010')
        if qs.filter(
            date_published__gte = date(2020, 1, 1)
        ).exists():
            yield ('2020+', 'Published recently after 2020')

    def queryset(self, request, queryset):
        if self.value() == '2000':
            return queryset.filter(
                date_published__gte = date(2000, 1, 1),
                date_published__lte = date(2010, 1, 1),
            )
        if self.value() == '2010':
            return queryset.filter(
                date_published__gte = date(2010, 1, 1),
                date_published__lte = date(2020, 1, 1,),
            )
        if self.value() == '2020+':
            return queryset.filter(
                date_published__gte = date(2020, 1, 1)
            )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    actions_on_bottom = False
    actions_selection_counter = True
    list_display = ['title', 'status', 'author', 'colored_color_details', 'author_list', '__str__']
    list_display_links = ['status']
    list_editable = ['author']
    fields = ['title','author',('status', 'date_published'), 'commentors']
    actions = [make_published, make_unpublished]
    date_hierarchy = 'date_published'
    empty_value_display = '-empty-'
    filter_horizontal = ('commentors',)
    filter_vertical = ('commentors',)
    list_filter = [DatePublishedFilter]
    preserve_filters = False
    radio_fields = {"status":admin.VERTICAL}
    autocomplete_fields = ['commentors']

    def get_actions(self, request):
        actions = super().get_actions(request)

        if not request.user.is_superuser:
            del actions['make_unpublished']
        return actions
    
    @admin.display(empty_value='???', description='Date Published')
    def value_date_published(self, obj):
        return obj.date_published

    value_date_published.short_description='Date Published'


@admin.register(Commentors)
class CommentorsAdmin(admin.ModelAdmin):
    search_fields = ['name']


class DecadeBornList(admin.SimpleListFilter):
    title = 'decade born'
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return [
            ('80s', "in the eighties"),
            ('90s', "in the nineties"),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '80s':
            return queryset.filter(
                birthday__gte=date(1980, 1, 1),
                birthday__lte=date(1990, 12, 31)
            )
        if self.value() == '90s':
            return queryset.filter(
                birthday__gte=date(1990, 1, 1),
                birthday__lte=date(1999, 12, 31),
            )
        
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = [DecadeBornList]
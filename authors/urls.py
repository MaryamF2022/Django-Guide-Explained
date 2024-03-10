from django.urls import path, re_path
from .views import DateListView, AuthorYearArchiveView, AuthorMonthArchiveView

urlpatterns = [
    path('', DateListView.as_view(), name='date-list'),
    re_path(r'^(?:year-(?P<year>\d{4}))$', AuthorYearArchiveView.as_view(), name='detail-author-year'),
    re_path(r"^(?:year-(?P<year>\d{4}))/(?:month-(?P<month>\d{2}))", AuthorMonthArchiveView.as_view(), name='detail-author-month')
]
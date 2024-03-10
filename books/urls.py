from django.urls import path
from .views import IndexView, BookDetailView, RedirectBookGenre, AddBookView, GenreView, UpdateBookView, DeleteBookView

app_name = 'books'

urlpatterns = [
    path('add/', AddBookView.as_view(), name='add'),
    # path('<str:genre>', IndexView.as_view(), name='ex2'),
    path('', IndexView.as_view(), name='ex2'),
    path('g/<str:genre>', GenreView.as_view(), name='genre-book'),
    path('<int:pk>/<slug:sl>', BookDetailView.as_view(), name='book-detail'),
    # path('g/<str:genre>', RedirectBookGenre.as_view(), name='genre-book'),
    path('<int:pk>/<slug:slug>/edit', UpdateBookView.as_view(), name='edit-detailed'),
    path('<int:pk>/<slug:slug>/delete', DeleteBookView.as_view(), name='delete-detailed')
]
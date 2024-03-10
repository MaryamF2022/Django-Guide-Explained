from django.urls import path
from . import views

urlpatterns = [
    path('mine/', views.MyView.as_view(), name='myview'),
    path('', views.HomePageView.as_view(), name='homepage')
]
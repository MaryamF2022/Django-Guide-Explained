from django.urls import path
from django.views.generic.base import TemplateView, RedirectView
from .views import Ex2View, PostPreLoadTaskView, SinglePostView

app_name = 'cbv'

urlpatterns = [
    path('ex1', TemplateView.as_view(template_name='ex1.html', 
                                     extra_context={'title': 'Custom Title'})),
    path('ex2', Ex2View.as_view(), name='ex2'),
    path('rdt', RedirectView.as_view(url='http://youtube.com/veryacademy'), name='go-to-very'),
    path('ex3/<int:pk>/', PostPreLoadTaskView.as_view(), name='redirect-task'),
    path('ex4/<int:pk>/', SinglePostView.as_view(),
         name='singlepost'),
]
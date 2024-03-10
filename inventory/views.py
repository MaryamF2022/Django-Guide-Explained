from typing import Any, Dict
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Singer, Answers, Question
from django.views.generic.detail import DetailView
# Create your views here.

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(f'Hello, World! {self.http_method_names}')
    
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['singers'] = Singer.objects.all()
        return context
    
class AnswerDatail(DetailView):
    model = Answers
    context_object_name = 'answer'
    template_name = 'answers.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.get(id=self.object.quest_id).name

        return context

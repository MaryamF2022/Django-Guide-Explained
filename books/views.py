from typing import Any, Dict, Optional, Type
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.db.models import F, Q
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .forms import AddForm
from .models import Books
from django.utils import timezone
from django import forms
from django.urls import reverse_lazy

# class AddBookView(FormView):
#     template_name = 'add.html'
#     form_class = AddForm
#     success_url ='/books/'
#     initial = {'title':'Title'}

#     def form_valid(self, form: Any) -> HttpResponse:
#         form.save()
#         return super().form_valid(form)

class DeleteBookView(DeleteView):
    success_url = '/books/'
    model = Books
    template_name = 'add.html'

    


class UpdateBookView(UpdateView):
    model = Books
    success_url = '/books/'
    form_class = AddForm
    template_name = 'add.html'

class AddBookView(CreateView):
    template_name = 'add.html'
    # form_class = AddForm
    model = Books
    fields =['title']
    success_url ='/books/'
    

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['title'].widget.attrs['class'] = 'form-control'
        return form


class IndexView(ListView):
    model = Books
    template_name = 'home.html'
    paginate_by = 2
    context_object_name = 'books'

    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     if kwargs.get('genre') != None:
    #         self.queryset = Books.objects.filter(genre__icontains = kwargs.get('genre'))
            
    #     return super().get(request, *args, **kwargs)
    
class GenreView(ListView):
    model = Books
    template_name = 'home.html'
    paginate_by = 2
    context_object_name = 'books'
    

    def get_queryset(self, *args, **kwargs):
        queryset = Books.objects.filter(genre__icontains=self.kwargs.get('genre'))
        return queryset

class RedirectBookGenre(RedirectView):
    pattern_name = 'books:ex2'
    query_string = True
    query_string = True

    
class BookDetailView(DetailView):

    model = Books
    template_name = 'book-detail.html'
    context_object_name = 'book'
    slug_field = 'slug' #Cannot resolve keyword 'myslug' into field. Choices are: author, count, genre, id, isbn, slug, title
    slug_url_kwarg = 'sl'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # book = Books.objects.filter(Q(slug=self.kwargs.get('sl')) & Q(pk = self.kwargs.get('pk')))
        # book.update(count=F('count') + 1)
        # context['book'] = book.get()

        context['time'] = timezone.now()

        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
       
    #     titles = [obj.id if obj.id != 6 else None for obj in queryset]
    #     if 6 in titles or 1 in titles:
    #         queryset = queryset.filter(author='Kevin')
        


    #     return queryset

    
    
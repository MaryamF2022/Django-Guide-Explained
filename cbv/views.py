from typing import Any, Dict, Optional
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Posts
from django.shortcuts import get_object_or_404
from django.db.models import F

class Ex2View(TemplateView):


    """
    TemplateResponseMixin Provides a mechanism to construct a TemplateResponse, given
    suitable context.
    Attributes:
    """

    template_name = "ex2.html"
    # template_engine = The NAME of the template engine to use for loading the template(Jinja2, Genshi)
    # response_class = Custome template loading or custome context object instantition TemplateResponse
    # content_type= Default Django uses 'text/html'

    """ get_context_data(**kwargs) is a method inherited from ContentMixins """

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['posts'] = Posts.objects.get()
        context['data'] = "Context Data for Ex2"
        return context
    
class PostPreLoadTaskView(RedirectView):
    # url = 'http://youtube.com/veryacademy'
    pattern_name = 'cbv:singlepost'
    # permanent = HTTP status code returned (True = 301, False = 302, Default = False)

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        # post = get_object_or_404(Posts, pk =kwargs['pk'])
        # post.count = F('count') + 1
        # post.save()

        post = Posts.objects.filter(pk=kwargs['pk'])
        post.update(count=F('count') + 1)
        return super().get_redirect_url(*args, **kwargs)
    
class SinglePostView(TemplateView):

    template_name = "ex4.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(Posts, pk = self.kwargs.get('pk'))
        return context
    

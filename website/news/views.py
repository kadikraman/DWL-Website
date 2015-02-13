from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class NewsView(TemplateView):
    template_name = 'news.html'
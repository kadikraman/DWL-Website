from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'about_us.html'
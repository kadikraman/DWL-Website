from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class GalleryView(TemplateView):
    template_name = 'gallery.html'
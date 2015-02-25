from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ServicesView(TemplateView):
    template_name = 'services.html'


class EventsView(TemplateView):
    template_name = 'events.html'


class PhotoshootsView(TemplateView):
    template_name = 'photoshoots.html'


class StylisticsView(TemplateView):
    template_name = 'stylistics.html'


class PublicRelationsView(TemplateView):
    template_name = 'public_relations.html'

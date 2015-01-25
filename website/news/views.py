from django.shortcuts import render
from django.http import HttpResponse
from news.models import Story

# Create your views here.
def index(request):
    latest_story_list = Story.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.title for p in latest_story_list])
    return HttpResponse(output)

def detail(request, story_id):
    return HttpResponse("The detail is: %s." % story_id)
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Entry


# Create your views here.
class NewsView(ListView):
    template_name = 'news.html'
    queryset = Entry.objects.order_by('-created_at')


class EntryDetail(DetailView):
    model = Entry
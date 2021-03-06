from django.db import models
from django.core.urlresolvers import reverse
from tinymce import models as tinymce_models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User')
    body = tinymce_models.HTMLField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "entries"

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'pk': self.pk})
from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=4000)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
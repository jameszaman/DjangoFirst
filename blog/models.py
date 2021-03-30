from django.db import models
from django.utils import timezone # for DateTimeFiled()
from django.contrib.auth.models import User #for author
from django.urls import reverse

# Create your models here.

class ToDo(models.Model):
   todotitle = models.CharField(max_length=100)
   todotext = models.TextField()
   date = models.DateTimeField(default=timezone.now)
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   status = models.CharField(max_length=100)

   def __str__(self):
      return self.title

   def get_absolute_url(self):
      return reverse('blog-detail', kwargs={'pk': self.pk})


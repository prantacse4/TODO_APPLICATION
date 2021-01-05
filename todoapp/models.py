from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    note = models.TextField()
    archive = models.IntegerField(default='0')
    date = models.CharField( max_length=50)
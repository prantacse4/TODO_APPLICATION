from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=254)
    note = models.TextField()
    archive = models.IntegerField(default='0')
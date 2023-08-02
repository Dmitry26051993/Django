from django.db import models

class Book(models.Model):
    page = models.CharField(max_length=75)
# Create your models here.

from django.db import models

# Create your models here.
class Library(models.Model):
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    publish_year = models.DateField()

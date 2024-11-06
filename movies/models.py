from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=255, unique=True)
    released_in = models.DateField()

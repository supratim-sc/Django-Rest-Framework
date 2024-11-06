from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255, unique=True)
    specalization = models.CharField(max_length=255)
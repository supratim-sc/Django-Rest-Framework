from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=5, unique=True)
    department = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
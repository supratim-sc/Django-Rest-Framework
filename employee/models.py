from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=255)
    emp_mail = models.EmailField(max_length=50, unique=True)
    designation = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.emp_name
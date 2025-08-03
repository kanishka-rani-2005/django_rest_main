from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    stdid=models.CharField(max_length=50)
    branch=models.CharField(max_length=100)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Standard(models.Model):
    name=models.CharField(max_length=266)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=266)
    age=models.IntegerField()
    standard=models.IntegerField()
    marks=models.IntegerField(null=True)

    def __str__(self):
        return self.name,self.age,self.standard,self.marks

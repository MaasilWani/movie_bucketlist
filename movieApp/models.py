from django.db import models
from django.core import validators
from django import forms

# Create your models here.
class Movie(models.Model):
    Name = models.CharField(max_length = 50)
    Actor = models.CharField(max_length=50)
    Actress = models.CharField(max_length=50)
    Date = models.DateField()
    Rating = models.IntegerField(validators=[validators.MaxValueValidator(10), validators.MinValueValidator(1)])
   
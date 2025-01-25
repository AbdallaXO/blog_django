from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.
class Post(models.Model):
    author = models.OneToOneField(
        Author, on_delete=models.CASCADE, null=False
        )
    content = models.CharField(max_length=5000)
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=300)
    date = models.DateField()
    image = models.ImageField()
    



class Country(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, unique=True)

class Author(models.Model):
    first_name = models.CharField(
        max_length=30,)
    last_name = models.CharField(
        max_length=30,)
    age = models.IntegerField(validators=[MinValueValidator(13)])
    country = models.OneToOneField(Country, on_delete=models.CASCADE, null=True)
    email = models.EmailField()
    
    

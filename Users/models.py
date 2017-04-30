from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class BasicInfo (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    age = models.IntegerField(validators=[MinValueValidator(2)])
    sex = models.BooleanField(default = False)
    createDate = models.DateTimeField(auto_now=False)
    updateDate = models.DateTimeField(auto_now=True)

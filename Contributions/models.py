from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import Users.models as userModel

# Create your models here.
class Classification_large(models.Model):
    name = models.CharField(max_length=200)

class Classification_middle(models.Model):
    name = models.CharField(max_length=200)
    largeClassId = models.ForeignKey(Classification_large, on_delete=models.CASCADE)

class Classification_small(models.Model):
    name = models.CharField(max_length=200)
    middleClassId = models.ForeignKey(Classification_middle, on_delete=models.CASCADE)
    alert = models.BooleanField(default = False)

class orderInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pay = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(50)])
    expense = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(50)], blank=True)
    image = models.ImageField(upload_to='images/')
    deadLine = models.DateField()
    createUser = models.ForeignKey(userModel.BasicInfo, on_delete=models.CASCADE)
    active = models.BooleanField(default = True)
    smallClassId = models.ForeignKey(Classification_small, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    isConfirm = models.BooleanField(default = False)

class replyInfo(models.Model):
    orderId = models.ForeignKey(orderInfo, on_delete=models.CASCADE)
    message = models.CharField(max_length=2000)
    createUser = models.ForeignKey(userModel.BasicInfo, on_delete=models.CASCADE)

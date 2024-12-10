from django.db import models
# Create your models here.
class Education(models.Model):
    degree = models.CharField(max_length=100,null=True,blank=True)
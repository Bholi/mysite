from django.db import models
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    nuber = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name
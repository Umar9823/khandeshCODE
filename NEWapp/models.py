from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

    
class Contact1(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    number = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=500)
      
    
    def __str__(self):
        return self.name     
    
    
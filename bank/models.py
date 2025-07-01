from django.db import models

# Create your models here.
class Customer(models.Model): 
    name = models.CharField(max_length=100) 
    dob = models.DateField() 
    email = models.EmailField(unique=True) 
    address = models.TextField() 
 
    def __str__(self): 
        return self.name
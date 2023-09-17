from django import forms
from django.db import models

# Create your models here.
class Signup(models.Model):
    fname  =models.CharField(max_length=122, null=False)
    lname = models.CharField(max_length=122)
    dob = models.DateField()
    phone =  models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    curr_address = models.CharField(max_length=1000)

    def __str__(self):
        return self.fname


    
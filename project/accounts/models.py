from django.db import models
from django.urls import reverse
from base.models import BaseModel

from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
class ShippingAddress(BaseModel):
        user=models.ForeignKey(to =User, on_delete=models.CASCADE)
        first_name=models.CharField(max_length=100)
        last_name=models.CharField(max_length=100)
        street=models.CharField(max_length=100)
        street_number=models.CharField(max_length=10)
        zip_code=models.CharField(max_length=20)
        city=models.CharField(max_length=50)
        country=CountryField()
        phone=models.CharField(max_length=30)
        current_address=models.BooleanField(default=False)

        def __str__(self):
            return f"{self.street}, {self.street_number}, {self.city}, {self.zip_code}, {self.country},{self.phone}"


class Profile(BaseModel):
    
    user = models.OneToOneField(to=User, on_delete=models.CASCADE,related_name="profile")
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    profile_image=models.ImageField(upload_to="profile",null=True,blank=True)
    bio=models.TextField(null=True,blank=True)
    shipping_address=models.ForeignKey(
        to=ShippingAddress, on_delete=models.CASCADE,null=True,blank=True
    )
    
    def _str_(self):
        return f"{self.user.username}"
    
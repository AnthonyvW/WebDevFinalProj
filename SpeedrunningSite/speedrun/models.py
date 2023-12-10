from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    pass

# class Profile(models.Model):
#     creator =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
#     profilePicture = models.ImageField()

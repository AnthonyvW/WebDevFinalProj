from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    pass

class Profile(models.Model):
     creator =  models.ForeignKey(User, on_delete=models.CASCADE)
     profilePicture = models.ImageField(upload_to="media/profile_pictures", default="media/default_pictures/default_user.jpeg")

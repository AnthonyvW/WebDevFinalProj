from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    pass

class Profile(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="media/profile_pictures", blank=True)

    # def getPic(self):
    #     return self.profile_picture

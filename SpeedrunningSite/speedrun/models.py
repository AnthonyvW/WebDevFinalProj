from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator 

class User(AbstractUser): 
    pass

class Profile(models.Model):
     creator =  models.ForeignKey(User, on_delete=models.CASCADE)
     profilePicture = models.ImageField(upload_to="media/profile_pictures", blank=True)

class Game(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(max_length=512)
    image = models.ImageField(upload_to='images/games')
    platforms = models.ManyToManyField('Platform', blank=True, related_name="platforms")

class Platform(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

class Speedrun(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="speedruns")
    time_in_seconds = models.IntegerField(validators=[MinValueValidator(0)])
    video_link = models.TextField(max_length=512)
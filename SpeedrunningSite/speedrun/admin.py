from django.contrib import admin
from .models import User, Game, Platform, Speedrun

# Register your models here.
admin.site.register(User)
admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Speedrun)

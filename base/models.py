from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(null=True, blank=True)
    profile_img = models.ImageField(default='default.jpg',null=True, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__ (self):
        return self.user.username

class Film(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    film_id = models.BigIntegerField()
    type_film = models.TextField()
    is_liked = models.BooleanField(default=False)
    is_watch = models.BooleanField(default=False)
    name = models.TextField()
    image = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    avatar = models.TextField(default='default.jpg')
    username = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


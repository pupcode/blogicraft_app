from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField( upload_to="images/user", null= True, blank = True, max_length=None)
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    other_names = models.CharField(max_length=100, default='', blank=True)
    phone_number = models.CharField(max_length=20, default='')
    bio = models.TextField(max_length=100, default='Hey there, I am a blogicraft User', blank=True)
    twitter_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
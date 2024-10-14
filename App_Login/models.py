from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    username = models.CharField(max_length = 264)
    full_name = models.CharField(max_length = 300)
    bio = models.TextField(blank=True)
    dob = models.DateField(blank=True, null=True)
    facebook_url = models.URLField(blank=True)

    def __str__(self):
        return self.username
    
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    created_date = models.DateTimeField(auto_now_add = True)

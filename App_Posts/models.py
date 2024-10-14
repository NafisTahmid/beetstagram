from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_author")
    image = models.ImageField(upload_to="post_photos")
    caption = models.CharField(max_length = 264, blank=True, null = True)
    upload_date = models.DateTimeField(auto_now = True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")

    def __str__(self):
        return '{}:{}'.format(self.user.username, self.post)
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    comment = models.TextField(blank= True, null = True)

    def __str__(self):
        return self.comment[:50]
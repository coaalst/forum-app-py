from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    post_title = models.CharField(max_length = 200)
    post_tweet = models.CharField(max_length = 200)
    post_user_id = models.ForeignKey(User, on_delete = models.CASCADE, default="")

    def __str__(self):
        return self.post_title


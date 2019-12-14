from django.db import models

class Post(models.Model):
    post_title = models.CharField(max_length = 200)
    post_tweet = models.CharField(max_length = 200)
    post_user_id = models.BigIntegerField()

    def __str__(self):
        return self.post_title

class User(models.Model):
    user_name = models.CharField(max_length = 200)
    user_password = models.CharField(max_length = 200)

    def __str__(self):
        return self.user_name
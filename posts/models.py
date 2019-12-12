from django.db import models

class Post(models.Model):
    post_titel = models.CharField(max_length = 200)
    post_tweet = models.CharField(max_length = 200)

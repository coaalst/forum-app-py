from django.db import models

class Post(models.Mode):
    post_id = models.PrimaryKey()
    post_titel = models.CharField(max_lenght = 200)
    post_tweet = models.CharField(max_lenght = 200)

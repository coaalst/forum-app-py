from django.db import models

class Post(models.Model):
    post_titel = models.CharField(max_length = 200)
    post_tweet = models.CharField(max_length = 200)
    post_user_id = models.BigIntegerField()

    def __str__(self):
        return self.post_titel

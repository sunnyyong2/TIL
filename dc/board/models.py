from django.db import models
from django.conf import settings

# Create your models here.


class Poster(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_posts')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.CASCADE)

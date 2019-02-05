from django.db import models
from django.conf import settings

class Post(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length = 30, default = writer)
    contents = models.TextField()




from django.contrib.auth.models import User
from django.db import models

class Link(models.Model):
    url =  models.URLField(unique = True)

    def __str__(self):
      return self.url

class Bookmark(models.Model):
    title = models.CharField( max_length = 200)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    link = models.ForeignKey(Link, on_delete = models.CASCADE)
from django.db import models

class link(models.Model):
    url =  models.URLField(unique = True)
# Create your models here.

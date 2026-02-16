from django.db import models

# Create your models here.

class Profile(models.Model):
    title = models.CharField(max_length = 30)
    description = models.TextField(blank = True, null = False)
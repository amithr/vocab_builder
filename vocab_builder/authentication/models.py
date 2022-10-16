from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.CharField(max_length=30)
    user_id = models.CharField(max_length=256)

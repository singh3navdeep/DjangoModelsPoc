from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=42)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

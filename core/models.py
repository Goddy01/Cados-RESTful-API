from django.db import models

# Create your models here.

class Advocate(models.Model):
    username =      models.CharField(max_length=255, unique=True, primary_key=True)
    bio =           models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username.title()
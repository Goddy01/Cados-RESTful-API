from django.db import models

# Create your models here.

class Company(models.Model):
    name =      models.CharField(max_length=255, unique=True)
    slogan =    models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name.title()

class Advocate(models.Model):
    company =       models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    username =      models.CharField(max_length=255, unique=True)
    bio =           models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username.title()
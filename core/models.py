from django.db import models

# Create your models here.

class Company(models.Model):
    name =      models.CharField(max_length=255, unique=True)
    slogan =    models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name.title()

class Advocate(models.Model):
    company =       models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    name =          models.CharField(max_length=255, unique=True, null=True, blank=True)
    username =      models.CharField(max_length=255, unique=True)
    twitter =       models.URLField(null=True, blank=True)
    bio =           models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username.title()
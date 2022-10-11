from email.policy import default
from unicodedata import category
from django.db import models

# Create your models here.


class MainInfo(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='uploads/', default="projects.jpg")

    def __str__(self):
        return self.title

class Resume(models.Model):
    file = models.FileField(upload_to='resume/')
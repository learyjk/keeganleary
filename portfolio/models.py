from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=200)
    link = models.CharField(max_length=255, default='#')
    github_link = models.URLField(max_length=255, default='', blank=True)
    long_description = models.TextField(default='', blank=True)

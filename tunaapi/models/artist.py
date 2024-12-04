from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=80)
  age = models.PositiveIntegerField()
  bio = models.CharField(max_length=800)

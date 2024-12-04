from django.db import models
from .artist import Artist

class Song(models.Model):
  title = models.CharField(max_length=200)
  artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
  album = models.CharField(max_length=50)
  length = models.PositiveIntegerField()

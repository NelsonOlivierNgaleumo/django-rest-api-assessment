"""View module for handling requests about songgenre"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import SongGenre


class SongGenreView(ViewSet):
    """Tuna Genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for songgenre

        Returns:
            Response -- JSON serialized songgenre
        """
        songgenre = SongGenre.objects.get(pk=pk)
        serializer = SongGenreSerializer(songgenre)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all songgenres

        Returns:
            Response -- JSON serialized list of songgenres
        """
        songgenre = SongGenre.objects.all()
        serializer = SongGenreSerializer(songgenre, many=True)
        return Response(serializer.data)
      
class SongGenreSerializer(serializers.ModelSerializer):
    """JSON serializer for song
    """
    class Meta:
        model = SongGenre
        fields = ('id', 'song_id', 'genre_id')

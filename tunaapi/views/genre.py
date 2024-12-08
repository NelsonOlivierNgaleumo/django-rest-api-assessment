"""View module for handling requests about genre"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Genre


class GenreView(ViewSet):
    """Tuna Genre view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single genre

        Returns:
            Response -- JSON serialized genre
        """
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all genres

        Returns:
            Response -- JSON serialized list of genres
        """
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized genre instance
        """

        genre = Genre.objects.create(
        description=request.data["description"],    
        )
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
 
    def update(self, request, pk):
        """Handle PUT requests for a genre

        Returns:
            Response -- Empty body with 204 status code
        """

        genre = Genre.objects.get(pk=pk)
        genre.description = request.data["description"]


        genre.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)   
class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for song
    """
    class Meta:
        model = Genre
        fields = ('id', 'description')

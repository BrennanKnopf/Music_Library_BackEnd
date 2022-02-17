from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'genre', 'release_date', 'likes']


    def create(self, validated_data):
        return Song.objects.create(**validated_data)
    
    def update(self, model, validated_data):
        model.title = validated_data.get('title', model.title)
        model.artist = validated_data.get('artist', model.artist)
        model.album = validated_data.get('album', model.album)
        model.genre = validated_data.get('genre', model.genre)
        model.releas_date = validated_data.get('release_date', model.release_date)
        model.likes = validated_data.get('likes', model.likes)
        model.save()
        return model

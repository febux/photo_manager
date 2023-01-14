from rest_framework import serializers

from photo_manager_api.models import Photo


class PhotoSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'date_created', 'user_created', 'image',)


class PhotoSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Photo.objects.create(**validated_data)

    class Meta:
        model = Photo
        fields = ('id', 'date_created', 'user_created', 'image', 'location', 'description', 'people_on_photo',)

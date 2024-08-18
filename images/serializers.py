from rest_framework import serializers
from .models import ImageModel

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'
        read_only_fields = ('processed_image', 'status')

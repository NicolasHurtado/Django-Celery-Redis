from django.shortcuts import render
from django.db import transaction

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ImageModel
from .serializers import ImageSerializer
from .tasks import process_image

class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_instance = serializer.save()
        process_image.delay(image_instance.id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

from django.shortcuts import render
from django.db import transaction

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ImageModel
from .serializers import ImageSerializer
from .tasks import process_image
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser

class ImageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing image instances.

    This viewset allows users to upload an image and process it asynchronously. 
    Processing includes operations such as applying filters or transformations
    (in this case converting to grayscale) to the uploaded image.
    """
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (FormParser, MultiPartParser)

    @swagger_auto_schema(
        operation_description="Create a new image process",
        responses={201: ImageSerializer()}
    )
    def create(self, request, *args, **kwargs):
        """
        Handle the creation of a new image.

        This endpoint allows a user to upload a new image. The image is saved,
        and a Celery task is triggered to process the image asynchronously. 
        The task applies a transformation to the image (e.g., converting it to grayscale).
        
        Returns:
            Response: A response object containing the serialized image data.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        image_instance = serializer.save()
        process_image.delay(image_instance.id)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

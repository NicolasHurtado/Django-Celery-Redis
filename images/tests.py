import pytest
from unittest.mock import patch, MagicMock
from images.tasks import process_image
from images.models import ImageModel
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

# Mock only the Celery task
@patch('images.views.process_image.delay')  # Adjust 'images.views' to where it is imported in your view
@pytest.mark.django_db
def test_upload_image(mock_process_image):
    client = APIClient()
    url = reverse('image-list')
    
    # Create a valid image in memory
    size = (800, 600)
    storage = BytesIO()
    img = Image.new("RGB", size)
    img.save(storage, "JPEG")
    storage.seek(0)
    file = SimpleUploadedFile(
        name="test_image.jpg", content=storage.getvalue(), content_type="image/jpeg"
    )
    
    # Send the POST request with the image
    response = client.post(url, {'original_image': file}, format='multipart')

    # Verify that the response is 201 Created
    assert response.status_code == status.HTTP_201_CREATED

    # Verify that process_image.delay was called once with the correct ID
    image_instance = response.data.get('id')  # Get the ID from the response
    mock_process_image.assert_called_once_with(image_instance)


@pytest.mark.django_db
@patch('images.tasks.Image.open')  # Mock Image.open to avoid the need for a real file
@patch('images.tasks.os.path.exists', return_value=True)  # Mock os.path.exists to always return True
def test_process_image_success(mock_exists, mock_open):
    # Create a mock ImageModel
    mock_image = MagicMock(spec=ImageModel)
    mock_image.id = 1
    mock_image.original_image.path = '/fake/path/to/image.jpg'
    mock_image.status = 0  # Initial status: Pending
    
    # Simulate retrieving the object from the database
    with patch('images.tasks.ImageModel.objects.get', return_value=mock_image):
        # Execute the processing task
        process_image(mock_image.id)
    
    # Verify that Image.open was called correctly with the file path
    mock_open.assert_called_once_with('/fake/path/to/image.jpg')
    
    # Verify that the save method was called to update the model
    assert mock_image.save.call_count == 1  # Should be called once: after processing
    
    # Verify that the status was updated to 'Processed'
    assert mock_image.status == 1

from celery import shared_task
from PIL import Image
import os
from .models import ImageModel
from django.conf import settings
import logging
import time

logger = logging.getLogger(__name__)

@shared_task
def process_image(image_id):
    """
    Asynchronously processes an image by applying a transformation.

    This task retrieves an image instance from the database using the provided 
    image ID. It then checks if the corresponding image file exists. If the file 
    exists, it applies a transformation (e.g., converting the image to grayscale) 
    and saves the processed image. The status of the image is updated based on 
    the success or failure of the operation.

    Args:
        image_id (int): The ID of the image to be processed.

    Raises:
        Exception: If any errors occur during the image processing, the error is logged,
                   and the status of the image is updated to indicate a failure.

    Workflow:
        1. Retrieve the image instance from the database.
        2. Verify if the image file exists.
        3. If the file exists, process the image (e.g., convert to grayscale).
        4. Save the processed image and update the image status to 'Processed'.
        5. If the file does not exist or an error occurs, update the image status to 'Error'.
    """
    time.sleep(10)  # Simulate delay for processing
    
    logger.info(f"todossss: {ImageModel.objects.all()}")
    try:
        logger.info(f"Processing image with ID: {image_id}")
        image_instance = ImageModel.objects.get(id=image_id)
        image_path = image_instance.original_image.path
        logger.info(f"Image path: {image_path}")

        # Check if the image exists
        if not os.path.exists(image_path):
            logger.error(f"Image not found at path: {image_path}")
            image_instance.status = 2  # 2 = Error
            image_instance.save()
            return

        # Process the image (example: convert to grayscale)
        img = Image.open(image_path).convert('L')
        output_path = os.path.splitext(image_path)[0] + '_processed.png'
        img.save(output_path)

        # Save the result
        image_instance.processed_image.name = output_path.split(settings.MEDIA_ROOT)[-1].lstrip('/')
        image_instance.status = 1  # 1 = Processed
        image_instance.save()

        logger.info(f"Image processed successfully: {output_path}")

    except Exception as e:
        logger.error(f"Error processing image with ID: {image_id}, Error: {str(e)}")
        if 'image_instance' in locals():
            image_instance.status = 2  # 2 = Error
            image_instance.save()

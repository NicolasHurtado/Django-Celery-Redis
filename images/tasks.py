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
    time.sleep(10)
    
    logger.info(f"todossss: {ImageModel.objects.all()}")
    try:
        logger.info(f"Processing image with ID: {image_id}")
        image_instance = ImageModel.objects.get(id=image_id)
        image_path = image_instance.original_image.path
        logger.info(f"Image path: {image_path}")

        # Verificar si la imagen existe
        if not os.path.exists(image_path):
            logger.error(f"Image not found at path: {image_path}")
            image_instance.status = 2  # 2 = Error
            image_instance.save()
            return

        # Procesamiento de la imagen (ejemplo: convertir a escala de grises)
        img = Image.open(image_path).convert('L')
        output_path = os.path.splitext(image_path)[0] + '_processed.png'
        img.save(output_path)

        # Guardar el resultado
        image_instance.processed_image.name = output_path.split(settings.MEDIA_ROOT)[-1].lstrip('/')
        image_instance.status = 1  # 1 = Processed
        image_instance.save()

        logger.info(f"Image processed successfully: {output_path}")

    except Exception as e:
        logger.error(f"Error processing image with ID: {image_id}, Error: {str(e)}")
        if 'image_instance' in locals():
            image_instance.status = 2  # 2 = Error
            image_instance.save()

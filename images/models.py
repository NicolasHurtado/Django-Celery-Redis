from django.db import models

# Create your models here.
class ImageModel(models.Model):
    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Processed'),
        (2, 'Error'),
    ]
    
    original_image = models.ImageField(upload_to='images/originals/')
    processed_image = models.ImageField(upload_to='images/processed/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
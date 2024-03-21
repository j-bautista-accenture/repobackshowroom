from django.db import models

# Create your models here.

class CompVisionU(models.Model):
    images = models.ManyToManyField('Image')
    
class Image(models.Model):
    imageName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='static/images/img1.jpeg')
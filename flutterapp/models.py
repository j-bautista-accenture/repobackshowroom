from django.db import models

# Create your models here.

class CompVisionF(models.Model):
    imageName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    modelSelected = models.CharField(max_length=100)

from rest_framework import serializers
from .models import CompVisionU, Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        #fields = ('modelname','path', 'description')
        fields = '__all__'

class CompVisionUSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = CompVisionU
        #fields = ('modelname','path', 'description')
        fields = '__all__'
        

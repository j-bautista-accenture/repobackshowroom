from rest_framework import serializers
from .models import CompVisionF

class CompVisionFSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompVisionF
        #fields = ('modelname','path', 'description')
        fields = '__all__'
from rest_framework import serializers
from .models import GenIA

class GenIASerializer(serializers.ModelSerializer):
    class Meta:
        model = GenIA
        fields = '__all__'
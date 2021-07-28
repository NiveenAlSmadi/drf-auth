  
from rest_framework import serializers

from .models import product

class makeupsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'brand', 'name', 'price', 'description','rating')
        model = product
from dataclasses import field
from rest_framework import serializers

from .models import Menuitem

class MenuitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menuitem
        fields = ('id', 'name', 'description', 'price', 'type', 'image')
        

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'
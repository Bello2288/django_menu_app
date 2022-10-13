from dataclasses import field
from rest_framework import serializers

from .models import Menuitem, Order

class MenuitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menuitem
        fields = ('id', 'name', 'description', 'price', 'type', 'image')
        

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
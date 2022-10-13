from django.shortcuts import render
from rest_framework import generics
from .models import Menuitem
from .serializers import MenuitemSerializer

# Create your views here.
class MenuitemListAPIView(generics.ListAPIView):
    queryset = Menuitem.objects.all()
    serializer_class = MenuitemSerializer



# class ReviewListCreateAPIView(generics.ListCreateAPIView):  # get request HTTP verb, and post
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

#self modules
from .models import *
from .serializer import ProductSerializer,ProductSerializerModel

class ProductViewSet(ModelViewSet):
    queryset= Product.objects.all()
    serializer_class= ProductSerializerModel
    permission_classes=[
        IsAuthenticated
    ]
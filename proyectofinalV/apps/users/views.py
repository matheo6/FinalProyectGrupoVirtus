from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
#self modules
from .models import *
from .serializer import *
from apps.restaurant.models import Order
from apps.restaurant.serializer import OrderSerializerModel

class UserViewSet(ModelViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializerModel
    permission_classes=[
        IsAuthenticated
    ]

class WaiterViewSet(ModelViewSet):
        queryset = Waiter.objects.all()
        serializer_class = WaiterSerializerModel

        @action(detail=True, methods=['post'])
        def add_shift(self, request, pk=None):
            waiter = self.get_object()
            request.data['waiter']=waiter.id
            serializer = Waiter_ShiftSerializerModel(data=request.data)            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        def get_serializer_class(self):
             print(self.request.query_params)
             return super().get_serializer_class()
        
        @action(detail=True, methods=['get'])
        def orders(self, request, pk=None):
            waiter = self.get_object()
            active = request.query_params.get('active')
            if active:
                orders = Order.objects.filter(waiter=waiter.id).filter(
                    models.Q(bill__isnull=True) | models.Q(bill__final_cost__isnull=True)
                )
            else:
                orders = Order.objects.filter(waiter=waiter.id)
            serializer = OrderSerializerModel(orders, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class WaiterShiftViewSet(ModelViewSet):
      queryset = Waiter_Shift.objects.all()
      serializer_class = Waiter_ShiftSerializerModel
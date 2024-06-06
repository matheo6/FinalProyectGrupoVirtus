from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
#self modules
from .models import *
from .serializer import *
from apps.users.models import Waiter_Shift,Waiter
from .permissions import isMG,isMG_AT

class RestaurantViewSet(ModelViewSet):
    queryset= Restaurant.objects.all()
    serializer_class=RestaurantSerializerModel
    permission_classes=[
        IsAuthenticated
    ]

class TableViewSet(ModelViewSet):
    queryset= Table.objects.all()
    serializer_class=TableSerializerModel
    permission_classes=[
        IsAuthenticated
    ]

class OrderViewSet(ModelViewSet):
    queryset= Order.objects.all()
    serializer_class=OrderSerializerModel
    permission_classes=[
        IsAuthenticated
    ]
    def destroy(self, request, pk=None):
        self.permission_classes+=[isMG_AT]
        return super().destroy(request)
    
    def filter_queryset(self, queryset):

        request_user=self.request.user
        queryset=super().filter_queryset(queryset)
        queryset= queryset.filter(ownerstask__user= request_user)
        return queryset

class BillsViewSet(ModelViewSet):
    queryset= Bill.objects.all()
    serializer_class=BillsSerializerModel
    permission_classes=[
        IsAuthenticated
    ]

    def destroy(self, request, pk=None):
                self.permission_classes += [isMG]
                self.check_permissions(request)
                
                bill = self.get_object()
                bill.delete()
                return Response({'Exito': 'Cuenta eliminada de manera exitosa'},status=status.HTTP_204_NO_CONTENT)
                        

class WaiterViewSet(ModelViewSet):
    queryset= Waiter.objects.all()
    serializer_class=WaiterSerializerModel
    permission_classes=[
        IsAuthenticated
    ]

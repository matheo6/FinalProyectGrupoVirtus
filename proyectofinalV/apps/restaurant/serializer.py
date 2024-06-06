from rest_framework import serializers
from .models import *

class RestaurantSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields="__all__"

class TableSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=Table
        fields="__all__"

class OrderSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"


class BillsSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=Bill
        fields="__all__"

class WaiterSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=Waiter
        fields="__all__"


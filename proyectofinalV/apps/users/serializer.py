from rest_framework import serializers
from .models import *

class UserSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class WaiterSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=Waiter
        fields="__all__"

class Waiter_ShiftSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=Waiter_Shift
        fields="__all__"

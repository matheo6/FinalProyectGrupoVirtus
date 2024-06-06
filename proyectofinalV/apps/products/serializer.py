from rest_framework import serializers

from .models import Product

class ProductSerializerModel(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= "__all__"


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    cost=serializers.CharField(max_length=60)
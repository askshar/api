from rest_framework.serializers import ModelSerializer

from .models import *


class ProductColourModelSerializer(ModelSerializer):
    class Meta:
        model = ProductColourModel
        fields = ['color']

class ProductImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = ['image']


class ProductMainModelSerializer(ModelSerializer):
    colors = ProductColourModelSerializer(many=True, read_only=True)
    images = ProductImageModelSerializer(many=True, read_only=True)
    class Meta:
        model = ProductMainModel
        fields = '__all__'


# class ProductMainModelDetailSerializer(ProductMainModelSerializer):
#     colors = ProductColourModelSerializer(many=True, read_only=True)
#     images = ProductImageModelSerializer(many=True, read_only=True)
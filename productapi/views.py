from rest_framework import generics

from .serializers import ProductMainModelSerializer
from .models import ProductMainModel


class Products(generics.ListAPIView):
    queryset = ProductMainModel.objects.all()
    serializer_class = ProductMainModelSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = ProductMainModel.objects.all()
    serializer_class = ProductMainModelSerializer
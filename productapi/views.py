from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductMainModelSerializer
from .models import ProductMainModel


@api_view(['GET'])
def product_view(request):

    products = ProductMainModel.objects.all()

    serializer = ProductMainModelSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, product_id):
    product = get_object_or_404(ProductMainModel, id=product_id)

    serializer = ProductMainModelSerializer(product)
    return Response(serializer.data)
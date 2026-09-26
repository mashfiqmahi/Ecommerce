from django.contrib.postgres import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    product_serializers = ProductSerializer(products, many=True)
    return Response(product_serializers.data)

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    category_serializers = CategorySerializer(categories, many=True)
    return Response(category_serializers.data)
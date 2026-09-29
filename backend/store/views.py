from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Category, Cart, CartItem
from .serializers import ProductSerializer, CategorySerializer, CartSerializer, CartItemSerializer

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

@api_view(['GET'])
def get_product(request,pk):
    try:
        product = Product.objects.get(id=pk)
        product_serializer = ProductSerializer(product, context={'request': request})
        return Response(product_serializer.data)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

@api_view(['GET'])
def get_cart(request):
    cart, created = Cart.objects.get_or_create(user=None)
    cart_serializer = CartSerializer(cart)
    return Response(cart_serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(user=None)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return Response({'message': 'Product added to cart', 'cart':CartSerializer(cart).data}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def remove_from_cart(request):
    item_id = request.data.get('item_id')
    CartItem.objects.filter(id=item_id).delete()
    return Response({'message': 'Item removed from cart'})

@api_view(['POST'])
def update_cart_quantity(request):
    item_id = request.data.get('item_id')
    quantity = request.data.get('quantity')
    if not item_id or quantity is None:
        return Response({'error': 'Item id or quantity is required'}, status=400)

    try:
        item = CartItem.objects.get(id=item_id)
        if int(quantity) < 1 :
            item.delete()
            return Response({'message': 'Quantity must be at least 1'}, status=400)
        item.quantity = quantity
        item.save()
        item_serializer = CartItemSerializer(item)
        return Response(item_serializer.data)
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=404)
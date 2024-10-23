from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

@api_view(['POST', 'GET', 'PUT', 'DELETE'])  # Allow all methods for this view
def product_handler(request):
    # Handle product creation (POST)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle product retrieval (GET)
    elif request.method == 'GET':
        product_id = request.query_params.get('id')
        product_name = request.query_params.get('name')

        if product_id:
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": 'Product with the given ID not found'}, status=status.HTTP_404_NOT_FOUND)
        elif product_name:
            try:
                product = Product.objects.get(name=product_name)
            except Product.DoesNotExist:
                return Response({"error": 'Product with the given name not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": 'ID or name required'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # Handle product update (PUT)
    elif request.method == 'PUT':
        product_id = request.data.get('id')
        product_name = request.data.get('name')

        if product_id:
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error": 'Product with the given ID not found'}, status=status.HTTP_404_NOT_FOUND)
        elif product_name:
            try:
                product = Product.objects.get(name=product_name)
            except Product.DoesNotExist:
                return Response({"error": 'Product with the given name not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": 'ID or name required'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle product deletion (DELETE)
    elif request.method == 'DELETE':
        product_id = request.data.get('id')
        product_name = request.data.get('name')

        if product_id:
            try:
                product = Product.objects.get(id=product_id)
                product.delete()
                return Response({'message': 'Product deleted successfully'}, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({'error': 'Product with the given ID not found'}, status=status.HTTP_404_NOT_FOUND)
        elif product_name:
            try:
                product = Product.objects.get(name=product_name)
                product.delete()
                return Response({'message': 'Product deleted successfully'}, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({'error': 'Product with the given name not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'ID or name required'}, status=status.HTTP_400_BAD_REQUEST)






        





#  product/viewsets/product_viewset.py
from rest_framework import viewsets

from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
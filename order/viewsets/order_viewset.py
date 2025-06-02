# order/order_viewset.py

#  Importando os ModelViewSet
from rest_framework.viewsets import ModelViewSet

#  Importando os modelos de Order
from order.models import Order

#  Importando os serializers
from order.serializers.order_serializer import OrderSerializer

# Criação do viewset de Order

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
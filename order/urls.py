# order/urls.py

from django.urls import path, include
from rest_framework import routers

from order import viewsets

router = routers.DefaultRouter()
router.register(r"order", viewsets.OrderViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]
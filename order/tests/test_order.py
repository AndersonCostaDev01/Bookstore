import pytest
from order.models import Order
from order.factories import OrderFactory, UserFactory
from product.factories import ProductFactory

@pytest.mark.django_db
def test_create_order_without_products():
    order = OrderFactory()
    assert isinstance(order, Order)
    assert order.user is not None
    assert order.product.count() == 0

@pytest.mark.django_db
def test_create_order_with_products():
    product1 = ProductFactory()
    product2 = ProductFactory()
    order = OrderFactory(products=[product1, product2])

    assert order.product.count() == 2
    assert product1 in order.product.all()
    assert product2 in order.product.all()

@pytest.mark.django_db
def test_order_user_is_linked():
    user = UserFactory()
    order = OrderFactory(user=user)

    assert order.user == user

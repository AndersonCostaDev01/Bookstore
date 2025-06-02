import pytest
from product.models import Product
from product.factories import ProductFactory, CategoryFactory

@pytest.mark.django_db
def test_create_product_without_categories():
    product = ProductFactory()
    assert isinstance(product, Product)
    assert product.title
    assert product.price
    assert product.categories.count() == 0

@pytest.mark.django_db
def test_create_product_with_categories():
    category1 = CategoryFactory()
    category2 = CategoryFactory()
    product = ProductFactory(categories=[category1, category2])

    assert product.categories.count() == 2
    assert category1 in product.categories.all()
    assert category2 in product.categories.all()

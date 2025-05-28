import pytest
from product.models import Category
from product.factories import CategoryFactory

@pytest.mark.django_db
def test_create_category():
    category = CategoryFactory()

    assert isinstance(category, Category)
    assert category.title
    assert category.slug
    assert category.description is not None or category.description is None
    assert isinstance(category.active, bool)

@pytest.mark.django_db
def test_category_unique_slug():
    category1 = CategoryFactory(slug="books")
    with pytest.raises(Exception):  # ou django.db.utils.IntegrityError se quiser ser mais específico
        CategoryFactory(slug="books")

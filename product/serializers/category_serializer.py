from rest_framework import serializers

# Importa o modelo de Categoria
from product.models.category import Category


# Cria um serializer para a categoria de produto
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Define o modelo que esse serializer representa

        # Campos da categoria que serão expostos na API
        fields = [
            "title",        # Nome da categoria
            "slug",         # Slug (URL amigável), geralmente gerado automaticamente
            "description",  # Descrição da categoria
            "active",       # Indica se a categoria está ativa ou não
        ]

        # Define que o campo "slug" não é obrigatório na criação via API
        # Pode ser útil se ele for gerado automaticamente no `save()` do modelo
        extra_kwargs = {"slug": {"required": False}}

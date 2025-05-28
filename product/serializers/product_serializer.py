from rest_framework import serializers

# Importa os modelos de Categoria e Produto
from product.models.product import Category, Product

# Importa o serializer da Categoria para exibir os dados dela no retorno da API
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    # Campo de leitura: exibe os detalhes das categorias associadas ao produto
    category = CategorySerializer(read_only=True, many=True)

    # Campo de escrita: o cliente envia apenas os IDs das categorias ao criar/editar
    categories_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),  # Garante que as categorias existem
        write_only=True,                 # Só aparece na entrada (POST/PUT)
        many=True                        # Permite múltiplas categorias
    )

    class Meta:
        model = Product  # Define o modelo que esse serializer representa
        fields = [
            "id",            # ID do produto
            "title",         # Título do produto
            "description",   # Descrição do produto
            "price",         # Preço
            "active",        # Se está ativo ou não
            "category",      # Dados completos das categorias (somente leitura)
            "categories_id", # Lista de IDs das categorias (somente escrita)
        ]

    # Método executado ao criar um novo produto via API
    def create(self, validated_data):
        # Remove os IDs das categorias do dicionário validado
        category_data = validated_data.pop("categories_id")

        # Cria o produto com os demais dados
        product = Product.objects.create(**validated_data)

        # Associa as categorias ao produto (ManyToMany)
        for category in category_data:
            product.category.add(category)

        # Retorna o produto criado
        return product

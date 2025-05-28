from rest_framework import serializers

# Importa o modelo de Order (Pedido)
from order.models import Order

# Importa o modelo de Product (Produto)
from product.models import Product

# Importa o serializer do produto para reutilizar aqui
from product.serializers.product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    # Campo de leitura: mostra os detalhes dos produtos no pedido
    # Usa o ProductSerializer para exibir os dados completos dos produtos
    product = ProductSerializer(read_only=True, many=True)

    # Campo de escrita: o cliente envia só os IDs dos produtos
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),  # Permite apenas produtos existentes
        write_only=True,                # Só é usado para entrada de dados (POST)
        many=True                       # Permite enviar vários produtos (lista)
    )

    # Campo que será calculado dinamicamente
    total = serializers.SerializerMethodField()

    # Método que calcula o total somando o preço de todos os produtos no pedido
    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order  # Define qual modelo esse serializer representa
        fields = ["product", "total", "user", "products_id"]  # Campos usados na API
        extra_kwargs = {
            "product": {"required": False}  # Ignora validação de 'product' ao criar
        }

    # Método executado quando um novo pedido é criado via API
    def create(self, validated_data):
        # Extrai a lista de produtos (recebida como IDs)
        product_data = validated_data.pop("products_id")

        # Extrai o usuário do pedido
        user_data = validated_data.pop("user")

        # Cria o pedido com o usuário
        order = Order.objects.create(user=user_data)

        # Associa cada produto ao pedido usando o ManyToMany
        for product in product_data:
            order.product.add(product)

        # Retorna o pedido criado
        return order

# Bookstore REST API

API REST para gerenciamento de uma livraria.

---

## Requisistos de sistema 

1. python3 

2. poetry 

## Como iniciar o projeto

1. Instale as dependências do projeto:

```
poetry install
```

2. Execute as migrações do banco de dados:

```
poetry run python manage.py migrate
```

3. Inicie o servidor de desenvolvimento:

```
poetry run python manage.py runserver
```

O servidor estará disponível em: `http://localhost:8000/`

---

## Rotas disponíveis

### Administração (Django Admin)

Acesse o painel administrativo padrão do Django em:

http://localhost:8000/admin/

---

### API de Pedidos (Orders)

- Versão 1 da API:  
http://localhost:8000/bookstore/v1/order/

- Versão 2 da API:  
http://localhost:8000/bookstore/v2/order/

---

### API de Produtos (Products)

- Versão 1 da API:  
http://localhost:8000/bookstore/v1/product/

- Versão 2 da API:  
http://localhost:8000/bookstore/v2/product/

---

Se precisar de ajuda para usar as rotas ou rodar o projeto, é só avisar!

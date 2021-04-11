# Projeto E-commerce (desafio backend)
Um projeto de e-commerce em python utilizando GraphQL utilizando: 

- Django 3.1.7
- Python 3.8.3
- ariadne 0.12.0
- ariadne-jwt 0.1.4


Banco de dados

- Postgresql 13-alpine


### TO DO's
Abaixo uma lista do que adicionei ou ainda pretendo adicionar.

- [x] Filtro de range com o campo price
- [x] Escrever testes automatizados para o graphql
- [x] Model de Categorias de produtos
- [x] Carrinho de compras baseado em session
- [x] Remover produtos do carrinho
- [x] Logout do cliente
- [x] Model de pagamento

### How to install
Abaixo uma os comandos necessários para clonar e configurar este projeto na sua 
máquina local:

- Instalar git, docker e docker-compose e depois:

```
git clone https://github.com/GeorgeSued14/desafio-backend.git
```

- Em seguida os seguintes comandos:

```
> cd desafio-backend
> docker-compose -f docker-compose.dev.yml build
> docker-compose -f docker-compose.dev.yml up -d 
> docker exec -it django /bin/sh -c "python manage.py makemigrations && 
python manage.py migrate"
``` 
- Para criar o usuário root da aplicação

```
docker exec -it django /bin/sh -c "python manage.py createsuperuser"
```

- No navegador digite:

```
http://localhost:8000/graphql
```

Pronto!

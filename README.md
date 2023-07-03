# API Imobiliaria Khanto


## Descrição

Foi utilizado o django com o framework DRF, a aplicação foi separada em tres apps, immobile, reserve e announcement. cada um dos apps implementa as operações de acordo com as regras de negocio descritas no desafio



## 💻 Pré-requisitos

  

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* docker `20.10.8+`
* docker-compose `1.29.2+`


  

<br>

  

## 🚀 Instalação

o arquivo de .env é utilizado para popular as variaveis necessarias para aplicação se conectar com o banco de dados e funcionar corretamente

<br>

  

  

### Clone este repositório usando ssh ou https

````

$ git clone git@github.com:Vinny1892/teste_tecnico_seazone.git

````

#### Acesse a pasta do projeto no terminal/cmd

```

$ cd teste_tecnico_seazone

```

  

<br>

  

### Para fazer build da imagem docker:

```docker

$ docker build -f docker/dockerfile.prod -t user/name-image

```

Aonde:

* User = Usuario dockerhub

* Name-image = Nome da imagem

  
  

<!-- Para instalar o projeto , siga estas etapas: -->

  

### Com docker:

  

<br>

  
  

#### Executa a aplicação em modo desenvolvimento

  

```

$ docker-compose up -d

```


## Execução dos testes e fixtures

Para execução dos testes e de outros comandos de forma simplificada no perojeto foi criado um `Makefile`, para rodar os testes só precisa rodar
```
make up-silent
make test
```

Para facilitar os testes também foram criados tres comandos utilizando a estrutura de comandos customizados do django, ele pode ser usado por dois jeitos
```bash
  make create-immobile NUMBER=5
  make create-announcement NUMBER=5
  make create-reserve NUMBER=5
```
Também pode ser feito direto pelo python

```bash
  python manage.py create_immobile 5
  python manage.py create_announcement 5
  python manage.py create_reserve 5
  
```
Foi criado um commando para criar os seeds de acordo com o documento do teste tecnico. esse comando não precisa ser rodado pois antes da aplicação ser iniciada ele ja irá ser chamado, em conjunto com  a criação das migraitons
```bash
 make db:seed
```



## 🛠 Tecnologias

  

As seguintes ferramentas foram usadas na construção do projeto:

  

- [Django](https://www.djangoproject.com/)

- [Django Rest Framework](https://www.django-rest-framework.org/)

- [Python](https://www.python.org/)

## Endpoints

 Após instalado a aplicação pode-se acessar os recursos listados abaixo
   - [reserve](http://localhost:8000/reserve) (http://localhost:8000/reserve)
   - [announcement](http://localhost:8000/announcement) (http://localhost:8000/announcement)
   - [immobile](http://localhost:8000/immobile) (http://localhost:8000/immobile)


## Modelo Immobile
O modelo `Immobile` representa uma propriedade imobiliária no sistema.

### Campos
- `id` (IntegerField): campo numerico gerado automaticamente pelo banco de dados
- `code` (IntegerField): Código único da propriedade.
- `quantity_toilet` (IntegerField): Quantidade de banheiros na propriedade.
- `accept_pet` (BooleanField): Indica se animais de estimação são permitidos na propriedade.
- `activation_date` (DateTimeField): Data de ativação da propriedade.
- `amount_clean` (DecimalField): Valor para limpeza da propriedade.
- `created_at` (DateTimeField): Data de criação do registro, são gerados automaticamente.
- `updated_at` (DateTimeField): Data de atualização do registro, são gerados automaticamente.
- 
#### Relacionamentos
O modelo `Immobile` possui os seguintes relacionamentos:

 - `announcement` (ForeignKey para Announcement): Relacionamento com o modelo Announcement.
### Exemplo de Uso

POST  http://localhost/immobile com o body abaixo

```json

{
  "code": 1234,
  "quantity_toilet": 2,
  "accept_pet": true,
  "activation_date": "2023-07-01T12:00:00Z",
  "amount_clean": 5000.50
}
````
também pode utilizar com o curl dessa forma.
```bash

curl -X POST -H "Content-Type: application/json" -d '{
  "code": 1234,
  "quantity_toilet": 2,
  "accept_pet": true,
  "activation_date": "2023-07-01T12:00:00Z",
  "amount_clean": 5000.50
}' http://localhost/immobile


```
para os outros recursos segue se a premissa do REST(representational state transfer) para acesso, atualização e deleção dos dados utilizando como base a url que foi disponibilizado na secão endpoints


## Modelo Announcement

O modelo `Announcement` representa um anúncio no sistema.

### Campos

- `tax_platform` (DecimalField): O valor da plataforma do anúncio (máximo de 6 dígitos com 2 casas decimais).
- `name_platform` (CharField): O nome da plataforma.
- `created_at` (DateTimeField): A data e hora em que o anúncio foi criado (gerado automaticamente quando o registro é criado).
- `updated_at` (DateTimeField): A data e hora em que o anúncio foi atualizado pela última vez (gerado automaticamente quando o registro é modificado).
- `immobile` (ForeignKey): O imóvel associado (relacionado ao modelo `Immobile`) por meio de uma relação de chave estrangeira.

### Exemplo de Uso

Você pode criar um novo anúncio enviando uma requisição POST para o endpoint `http://localhost/announcement` com o seguinte corpo (body):

```json
{
  "tax_platform": 99.99,
  "name_platform": "Nome da Plataforma",
  "immobile": 1
}
```

```bash

curl -X POST -H "Content-Type: application/json" -d '{
  "tax_platform": 99.99,
  "name_platform": "Nome da Plataforma",
  "immobile": 1
}' http://localhost/announcement

```
para os outros recursos segue se a premissa do REST(representational state transfer) para acesso, atualização e deleção dos dados utilizando como base a url que foi disponibilizado na secão endpoints


## Modelo Reserve

O modelo `Reserve` representa uma reserva no sistema.

### Campos

- `code` (UUIDField): O código único da reserva, gerado automaticamente no momento da criação.
- `quantity_guests` (IntegerField): A quantidade de hóspedes na reserva.
- `total_price` (DecimalField): O preço total da reserva (máximo de 6 dígitos com 2 casas decimais).
- `comment` (CharField): Um comentário opcional para a reserva.
- `check_in` (DateTimeField): A data e hora de check-in da reserva.
- `check_out` (DateTimeField): A data e hora de check-out da reserva.
- `created_at` (DateTimeField): A data e hora em que a reserva foi criada (gerado automaticamente quando o registro é criado).
- `updated_at` (DateTimeField): A data e hora em que a reserva foi atualizada pela última vez (gerado automaticamente quando o registro é modificado).
- `announcement` (ForeignKey): O anúncio associado (relacionado ao modelo `Announcement`) por meio de uma relação de chave estrangeira.

### Exemplo de Uso

Você pode criar uma nova reserva enviando uma requisição POST para o endpoint `http://localhost/reserve` com o seguinte corpo (body):

```json
{
  "quantity_guests": 2,
  "total_price": 99.99,
  "comment": "Este é um comentário",
  "check_in": "2023-07-01T10:00:00Z",
  "check_out": "2023-07-03T12:00:00Z",
  "announcement": 1
}
```   
```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "quantity_guests": 2,
  "total_price": 99.99,
  "comment": "Este é um comentário",
  "check_in": "2023-07-01T10:00:00Z",
  "check_out": "2023-07-03T12:00:00Z",
  "announcement": 1
}' http://localhost/reserve
```
para os outros recursos segue se a premissa do REST(representational state transfer) para acesso, atualização e deleção dos dados utilizando como base a url que foi disponibilizado na secão endpoints

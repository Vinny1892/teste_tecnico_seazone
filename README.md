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
para os outros recursos segue se a premissa do REST(representational state transfer) para acesso, atualização e deleção dos dados 




   


# cronos_api

API para gerenciamento de Serviços, Posts e Integrantes da Equipe, permitindo que o administrador do site consiga criar, editar, deletar e visualizar os dados através de um painel administrativo.

## Stack utilizada

- Python
- Django
- DRF
- Postgrees
- Docker e docker-compose
- Github Actions(Testes automatizados)
- Swagger
- Redoc

## Instalação de requisitos (NECESSÁRIO:Python 3.7.0+ e pip(Atualizado))

- Crie um ambiente virtual de sua preferência (Recomendado/Opcional)

- Faça a instalação do `requirements.txt` usando o comando: `pip install -r requirements.txt`

## Criando banco de dados

- Rode as migrações do projeto: `python manage.py migrate`

## Criando superusuário

- Rode: `python manage.py initadmin`
- Será gerado um admin username: `admin` e password: `admin123`

## Carregando dados iniciais

- Carregar arquivo de fixtures com: `python manage.py loaddata fixtures.yaml`

## Rodando os testes unitários

- Rode as migrações do projeto: `python manage.py test`

## Rodando o server

- Rode: `python manage.py runserver`

## Rodando o server com docker-compose

- Rode: `docker-compose up`
- Este comando sobe um container postegres e o container do projeto backend

## Documentação

- Documenntação swagger: `localhost:8000/swagger/`
- Documenntação redoc: `localhost:8000/redoc/`
- OBS: Para testar a api no swagger, após se autenticar no endpoint `POST api/token/` usar o prefixo Bearer. ex: `Bearer <TOKEN>`

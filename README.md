# ObraSpecAPI

## Descrição

ObraSpecAPI é uma API REST desenvolvida com o framework Django REST Framework (DRF). O projeto visa fornecer uma interface para gerenciamento de especificações de obras, permitindo operações CRUD (Create, Read, Update, Delete) em dados relacionados a projetos de construção, especificações técnicas e afins. 

O repositório contém a estrutura básica de um projeto Django, incluindo configurações para autenticação, serialização de dados e endpoints API personalizados.

## Tecnologias Utilizadas

- **Python**: Versão 3.8 ou superior.
- **Django**: Framework web para desenvolvimento rápido.
- **Django REST Framework**: Extensão para construção de APIs RESTful.
- **Banco de Dados**: SQLite por padrão (configurável para PostgreSQL, MySQL, etc.).
- Outras dependências: Listadas no arquivo `requirements.txt` (ex.: djangorestframework, etc.).

## Pré-requisitos

- Python 3.x instalado.
- Git instalado para clonar o repositório.
- Opcional: Um ambiente virtual (venv) para isolar dependências.

## Instalação

1. Clone o repositório:

   ```
   git clone https://github.com/Squad15-JotaNunes/ObraSpecAPI.git
   cd ObraSpecAPI
   ```

2. Crie e ative um ambiente virtual:

   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

4. Aplique as migrações do banco de dados:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Crie um superusuário para acessar o admin:

   ```
   python manage.py createsuperuser
   ```

## Uso

1. Inicie o servidor de desenvolvimento:

   ```
   python manage.py runserver
   ```

2. Acesse a API no navegador ou via ferramentas como Postman/Insomnia:
   - URL base: `http://127.0.0.1:8000/api/`
   - Admin Django: `http://127.0.0.1:8000/admin/` (faça login com o superusuário).

## Endpoints da API

Assumindo uma estrutura padrão de app Django (ajuste conforme os modelos implementados no projeto, como em `models.py`):

- **GET /api/especificacoes/**: Lista todas as especificações de obras.
- **POST /api/especificacoes/**: Cria uma nova especificação.
- **GET /api/especificacoes/{id}/**: Retorna detalhes de uma especificação específica.
- **PUT /api/especificacoes/{id}/**: Atualiza uma especificação.
- **DELETE /api/especificacoes/{id}/**: Exclui uma especificação.

Para autenticação, use tokens ou sessões (configurado no DRF). Teste os endpoints com ferramentas de API.

## Testes

Execute os testes unitários:

```
python manage.py test
```

# TradeGuard

Sistema de gerenciamento de contratos e fornecedores desenvolvido com Django como projeto de estudo para portfolio.

## Sobre

TradeGuard é um projeto focado em explorar os conceitos centrais do Django em um contexto real de negócios: gestão de contratos. O sistema permite cadastrar fornecedores, vincular contratos com upload de documentos, e visualizar tudo de forma organizada.

## Tecnologias

- **Django 6.0** — Framework web (Models, Views, Templates, Admin, Auth customizada)
- **PostgreSQL 18** — Banco de dados relacional
- **Docker / Docker Compose** — Containerização do ambiente
- **python-decouple** — Gestão de variáveis de ambiente
- **django-extensions** — Utilitários extras (shell_plus)
- **Ruff** — Linter e formatador
- **UV** — Gerenciador de pacotes Python

## Funcionalidades

- Autenticação customizada com login por e-mail (model `User` extendendo `AbstractUser`)
- Cadastro de fornecedores (CNPJ único, e-mail, nome corporativo)
- Cadastro de contratos vinculados a fornecedores com:
  - Número do contrato, descrição, valor
  - Datas de vigência (início/fim)
  - Status (Ativo / Suspenso / Encerrado)
  - Upload de documento (PDF, etc.) organizado por data
- Listagem de contratos com filtros e busca
- Página de detalhe do contrato com dados do fornecedor e documento anexo
- Admin Django completo e customizado
- Interface com tema escuro

## Estrutura do Projeto

```
tradeguard/
├── core/                    # Configuração central do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py / asgi.py
├── users/                   # App de autenticação
│   ├── models.py            # User (AbstractUser com email como USERNAME_FIELD)
│   └── admin.py
├── management/              # App principal (contratos e fornecedores)
│   ├── models.py            # Supplier e Contract
│   ├── views.py             # get_contracts, get_contract_detail
│   ├── urls.py
│   ├── admin.py             # Admin com inlines e filtros
│   ├── templates/           # listContracts.html, contractDetail.html
│   └── static/              # CSS tema escuro
├── templates/               # Template base (base.html)
├── media/                   # Uploads de documentos
├── compose.yml              # Docker Compose (PostgreSQL + Django)
├── Dockerfile               # Imagem Docker
└── start.sh                 # Entrypoint (migrate + runserver)
```

## Modelos

```python
User      # id (UUID), email (unique), username, password, ...
Supplier  # id (UUID), corporate_name, cnpj (unique), email (unique), created_at
Contract  # id (UUID), supplier (FK), contract_number, description,
          # contract_value, document (FileField), contract_status (choices),
          # start_date, end_date
```

## Como Rodar

### Com Docker (recomendado)

```bash
docker compose up --build
```

Acesse em [http://localhost:8080](http://localhost:8080)

### Sem Docker

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # ou configure manualmente
python manage.py migrate
python manage.py runserver
```

Crie um superusuário para acessar o admin:

```bash
python manage.py createsuperuser
```

## .env

O projeto usa `python-decouple`. Configure as variáveis no `.env`:

```env
SECRET_KEY=sua-chave-aqui
DEBUG_MODE=True
DB_NAME=tradeguard
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

# HabitForge 🦾

HabitForge é uma API REST construída com FastAPI para gerenciar hábitos diários, usuários e execuções, com autenticação via OAuth2 + JWT.  
O projeto está publicado em produção em:

- **API base**: `https://habitforge-4zm5.onrender.com/api`
- **Swagger UI**: `https://habitforge-4zm5.onrender.com/api/docs`

## Tecnologias

- FastAPI
- Python (async)
- SQLAlchemy + asyncpg
- PostgreSQL (Neon)
- Alembic (migrações)
- OAuth2 + JWT (PyJWT)
- passlib[bcrypt] para hash de senha

## Funcionalidades

- Cadastro de usuários com senha criptografada
- Autenticação com JWT
- CRUD de hábitos vinculados ao usuário autenticado
- Documentação automática via Swagger (OpenAPI)

## Endpoints principais

Prefixo geral: `/api`

- `POST /api/auth/signup` – cria usuário
- `POST /api/auth/login` – login (OAuth2 password flow, retorna access_token)
- `GET /api/users/` – lista usuários (apenas exemplo)
- `GET /api/users/{user_id}` – busca usuário por id
- `POST /api/habits/` – cria hábito do usuário logado
- `GET /api/habits/` – lista hábitos do usuário logado
- `GET /api/habits/{habit_id}` – detalhe de um hábito
- `DELETE /api/habits/{habit_id}` – apaga hábito

## Como rodar localmente

1. Clonar o repositório:

```bash
git clone <sua-url-github>
cd HabitForge
```

2. Criar e ativar o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou source venv/bin/activate no Linux/macOS
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Criar arquivo `.env` na raiz:

```env
DATABASE_URL=postgresql+asyncpg://usuario:senha@host:5432/dbname?sslmode=require
```

5. Rodar as migrações:

```bash
alembic upgrade head
```

6. Subir o servidor:

```bash
uvicorn app.main:app --reload
```

- API local: `http://127.0.0.1:8000/api`
- Swagger local: `http://127.0.0.1:8000/api/docs`

## Fluxo de autenticação

1. `POST /api/auth/signup` para criar um usuário.
2. `POST /api/auth/login` com `username` (email) e `password`.
3. Copiar `access_token` retornado.
4. No Swagger, clicar em **Authorize** e informar `Bearer <access_token>`.
5. Usar as rotas de `/api/habits` autenticado.

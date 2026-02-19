# Mini CRM Leads API

API profissional para gerenciamento de leads de uma revenda de veículos, desenvolvida com FastAPI, SQLite e arquitetura em camadas.

Projeto criado com foco em boas práticas de desenvolvimento backend, validação de dados, autenticação, testes automatizados e estrutura pronta para deploy.

---

## Tecnologias utilizadas

* Python 3.13
* FastAPI
* SQLite
* Pydantic
* Pytest
* Uvicorn
* Dotenv

---

## Funcionalidades

* Criar leads
* Listar leads
* Atualizar leads
* Soft delete de leads
* Filtros múltiplos
* Paginação
* Estatísticas com GROUP BY
* Validação com Pydantic
* Autenticação com API Key
* Logging
* Testes automatizados
* Health check endpoint
* Arquitetura profissional em camadas

---

## Estrutura do projeto

```
mini-crm-api/

app/
│
├── main.py
├── models.py
├── config.py
├── database.py
├── schemas.py
├── logger.py
├── security.py
│
├── routes/
│   └── leads.py
│
├── services/
│   └── leads_service.py
│
tests/
│   ├── test_leads.py
│   └── test_health.py
│
.env
requirements.txt
README.md
.gitignore
```

---

## Como rodar o projeto

### 1 — Clonar repositório

```
git clone https://github.com/seuusuario/mini-crm-api.git
```

### 2 — Entrar na pasta

```
cd mini-crm-api
```

### 3 — Criar ambiente virtual

```
python -m venv venv
```

### 4 — Ativar ambiente

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 5 — Instalar dependências

```
pip install -r requirements.txt
```

### 6 — Rodar servidor

```
uvicorn app.main:app --reload
```

---

## Documentação da API

Após iniciar o servidor, acessar:

```
http://127.0.0.1:8000/docs
```

Interface interativa Swagger.

---

## Autenticação

A API usa API Key.

Header obrigatório:

```
x-api-key: 123456
```

---

## Endpoints principais

### Criar lead

```
POST /leads
```

### Listar leads

```
GET /leads
```

Suporta filtros:

```
/leads?status=novo&page=1&limit=10
```

---

### Atualizar lead

```
PATCH /leads/{id}
```

---

### Deletar lead (soft delete)

```
DELETE /leads/{id}
```

---

### Estatísticas

```
GET /leads/stats
```

Retorna contagem por status.

---

### Health Check

```
GET /health
```

Retorna status da API.

---

## Testes automatizados

Rodar:

```
pytest
```

---

## Arquitetura utilizada

* Routes → Endpoints
* Services → Regras de negócio
* Schemas → Validação
* Database → Conexão
* Security → Autenticação
* Logger → Logs
* Tests → Testes automatizados

---

## Objetivo do projeto

Projeto desenvolvido para estudo e aplicação de conceitos profissionais de backend, incluindo:

* construção de APIs REST
* organização em camadas
* autenticação
* validação de dados
* testes automatizados
* preparação para frontend e deploy

---

## Próximos passos

* Frontend em React
* Deploy em cloud
* Banco PostgreSQL
* Autenticação JWT
* Dashboard

---

## Autor

Luis Eduardo Brescansin Canal

Projeto para fins educacionais e portfólio.

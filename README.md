# Minas Store Infra API

API REST desenvolvida para o Trabalho Final da disciplina de Cloud Computing.

## Tema

Infraestrutura para um Pequeno E-Commerce.

A API simula a consulta de componentes de infraestrutura necessários para manter um pequeno e-commerce em ambiente de nuvem, como servidor web, banco de dados, backup, monitoramento, CDN, DNS e pipeline de integração contínua.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Pytest
- Ruff
- GitHub Actions
- Docker

## Estrutura do projeto

```text
trabalho-final-cloud-api/
├── api/
│   ├── app.py
│   ├── __init__.py
│   └── data/
│       └── componentes.json
├── tests/
│   └── test_api.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── requirements.txt
└── README.md
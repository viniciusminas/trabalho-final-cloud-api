from json import JSONDecodeError
import json
from pathlib import Path

from fastapi import FastAPI, HTTPException


app = FastAPI(
    title="Minas Store Infra API",
    description="API REST para consulta de componentes de infraestrutura de um pequeno e-commerce.",
    version="1.0.0",
)

DATA_FILE = Path(__file__).parent / "data" / "componentes.json"


def carregar_componentes() -> list[dict]:
    try:
        with DATA_FILE.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, JSONDecodeError) as erro:
        raise HTTPException(
            status_code=500,
            detail={
                "sucesso": False,
                "mensagem": "Erro interno ao carregar os dados da API.",
                "erro": str(erro),
            },
        ) from erro


@app.get("/status")
def status():
    return {
        "sucesso": True,
        "dados": {
            "nome": "Minas Store Infra API",
            "versao": "1.0.0",
            "status": "online",
        },
    }


@app.get("/componentes")
def listar_componentes():
    componentes = carregar_componentes()

    return {
        "sucesso": True,
        "total": len(componentes),
        "dados": componentes,
    }


@app.get("/componentes/{componente_id}")
def buscar_componente_por_id(componente_id: int):
    componentes = carregar_componentes()

    for componente in componentes:
        if componente["id"] == componente_id:
            return {
                "sucesso": True,
                "dados": componente,
            }

    raise HTTPException(
        status_code=404,
        detail={
            "sucesso": False,
            "mensagem": "Componente de infraestrutura não encontrado.",
        },
    )
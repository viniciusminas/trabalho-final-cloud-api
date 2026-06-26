from fastapi.testclient import TestClient

from api.app import app


client = TestClient(app)


def test_listar_componentes_retorna_status_200():
    resposta = client.get("/componentes")

    assert resposta.status_code == 200


def test_listar_componentes_retorna_estrutura_json_esperada():
    resposta = client.get("/componentes")
    corpo = resposta.json()

    assert "sucesso" in corpo
    assert "total" in corpo
    assert "dados" in corpo
    assert corpo["sucesso"] is True
    assert isinstance(corpo["dados"], list)
    assert len(corpo["dados"]) >= 10


def test_buscar_componente_inexistente_retorna_404():
    resposta = client.get("/componentes/999")

    assert resposta.status_code == 404


def test_buscar_componente_por_id_retorna_dados_corretos():
    resposta = client.get("/componentes/1")
    corpo = resposta.json()

    assert resposta.status_code == 200
    assert corpo["sucesso"] is True
    assert corpo["dados"]["id"] == 1
    assert corpo["dados"]["nome"] == "Servidor Web"
    assert corpo["dados"]["criticidade"] == "Alta"
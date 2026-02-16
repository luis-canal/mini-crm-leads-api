import requests

BASE_URL = "http://127.0.0.1:8000"


def test_criar_lead():
    response = requests.post(
        f"{BASE_URL}/leads",
        json={
            "nome": "Luis",
            "telefone": "999999999",
            "carro": "Civic",
            "status": "novo"
        }
    )

    assert response.status_code == 200


def test_listar_leads():
    response = requests.get(f"{BASE_URL}/leads")

    assert response.status_code == 200


def test_estatisticas():
    response = requests.get(f"{BASE_URL}/leads/stats")

    assert response.status_code == 200

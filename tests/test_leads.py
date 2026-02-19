import requests

BASE_URL = "http://127.0.0.1:8000"

headers = {
    "x-api-key": "123456"
}

def test_criar_lead():

    response = requests.post(
        f"{BASE_URL}/leads",
        json={
            "nome": "Luis",
            "telefone": "999999999",
            "carro": "Civic",
            "status": "novo"
        },
        headers=headers
    )

    print(response.text)  # debug opcional

    assert response.status_code == 200


def test_listar_leads():

    response = requests.get(
        f"{BASE_URL}/leads",
        headers=headers
    )

    print(response.text)

    assert response.status_code == 200


def test_stats():

    response = requests.get(
        f"{BASE_URL}/leads/stats",
        headers=headers
    )

    print(response.text)

    assert response.status_code == 200

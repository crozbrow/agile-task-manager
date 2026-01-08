import json
import sys
import os

# Adiciona a raiz do projeto ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app import app


def test_create_task():
    client = app.test_client()

    response = client.post(
        "/tasks",
        data=json.dumps({
            "title": "Teste Automatizado",
            "priority": "Alta"
        }),
        content_type="application/json"
    )

    assert response.status_code == 201

    data = response.get_json()
    assert data["title"] == "Teste Automatizado"
    assert data["priority"] == "Alta"

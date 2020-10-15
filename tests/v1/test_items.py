from uuid import uuid4

from starlette.testclient import TestClient

from tests.v1.factories import ItemFactory


def test_no_items(client: TestClient):
    request = client.get("/v1/items")
    assert request.status_code == 404

    request = client.get(f"/v1/items/{str(uuid4())}")
    assert request.status_code == 404

    request = client.put(
        f"/v1/items/{str(uuid4())}", json=ItemFactory.mock_item)
    assert request.status_code == 404

    request = client.delete(f"/v1/items/{str(uuid4())}")
    assert request.status_code == 404


def test_create_item(client: TestClient):
    request = client.post("/v1/items", json=ItemFactory.mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "An Item"
    assert data.get("created_at")
    assert data.get("updated_at")


def test_get_item(client: TestClient):
    request = client.post("/v1/items", json=ItemFactory.mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "An Item"

    item_id = data.get("id")
    request = client.get(f"/v1/items/{item_id}")
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "An Item"


def test_list_items(client: TestClient):
    request = client.get("/v1/items")
    assert request.status_code == 200
    assert len(request.json()) == 2


def test_update_item(client: TestClient):
    request = client.post("/v1/items", json=ItemFactory.mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("desc") == "A quite common item."

    item_id = data.get("id")
    request = client.put(f"/v1/items/{item_id}",
                         json=ItemFactory.updated_mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("desc") == "A very peculiar item."


def test_delete_item(client: TestClient):
    request = client.post("/v1/items", json=ItemFactory.mock_item)
    assert request.status_code == 200
    data = request.json()
    item_id = data.get("id")

    request = client.delete(f"/v1/items/{item_id}")
    assert request.status_code == 200

    request = client.get("/v1/items")
    assert request.status_code == 200
    assert item_id not in [item.get("id") for item in request.json()]

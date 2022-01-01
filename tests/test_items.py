from uuid import uuid4

from starlette.testclient import TestClient

from firestorefastapi.schemas.item import ItemCreate, ItemUpdate

mock_item = ItemCreate.Config.schema_extra["example"]
mock_item_update = ItemUpdate.Config.schema_extra["example"]


def test_no_items(client: TestClient) -> None:
    request = client.get("/items")
    assert request.status_code == 404

    request = client.get(f"/items/{str(uuid4())}")
    assert request.status_code == 404

    request = client.put(f"/items/{str(uuid4())}", json=mock_item)
    assert request.status_code == 404

    request = client.delete(f"/items/{str(uuid4())}")
    assert request.status_code == 404


def test_create_item(client: TestClient) -> None:
    request = client.post("/items", json=mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "An Item"
    assert data.get("created_at")
    assert data.get("updated_at")


def test_get_item(client: TestClient) -> None:
    request = client.post("/items", json=mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "An Item"

    item_id = data.get("id")
    request = client.get(f"/items/{item_id}")
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "An Item"


def test_list_items(client: TestClient) -> None:
    request = client.get("/items")
    assert request.status_code == 200
    assert len(request.json()) == 2


def test_update_item(client: TestClient) -> None:
    request = client.post("/items", json=mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("desc") == "A quite common item."

    item_id = data.get("id")
    request = client.put(f"/items/{item_id}", json=mock_item_update)
    assert request.status_code == 200
    data = request.json()
    assert data.get("desc") == "A very peculiar item."


def test_delete_item(client: TestClient) -> None:
    request = client.post("/items", json=mock_item)
    assert request.status_code == 200
    data = request.json()
    item_id = data.get("id")

    request = client.delete(f"/items/{item_id}")
    assert request.status_code == 200

    request = client.get("/items")
    assert request.status_code == 200
    assert item_id not in [item.get("id") for item in request.json()]

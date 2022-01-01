from starlette.testclient import TestClient


def test_healthcheck(client: TestClient):
    request = client.get("/healthcheck")
    response = request.json()
    assert response.get("message") == "healthy"
    assert response.get("version")
    assert response.get("time")

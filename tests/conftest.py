import pytest
from starlette.testclient import TestClient

from firestorefastapi.database import db
from firestorefastapi.main import api


@pytest.fixture()
def client():
    with TestClient(api) as client:
        yield client


@pytest.fixture(scope="module", autouse=True)
def reset_mock_firestore():
    db.reset()

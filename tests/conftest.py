import pytest
from starlette.testclient import TestClient

from database import db
from main import api


@pytest.fixture()
def client():
    """
    When using the "client" fixture in test cases, we'll get full database
    rollbacks between test cases
    """
    with TestClient(api) as client:
        yield client


@pytest.fixture(scope="module", autouse=True)
def reset_mock_firestore():
    db.reset()


from calculator import add, subtract, multiply, divide
from app import app


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    assert divide(5, 0) == "Error"


def test_homepage():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_calculate_api():
    client = app.test_client()

    response = client.post(
        "/calculate",
        json={
            "operation": "add",
            "a": 10,
            "b": 5
        }
    )

    assert response.status_code == 200
    assert response.get_json()["result"] == 15


def test_invalid_operation():
    client = app.test_client()

    response = client.post(
        "/calculate",
        json={
            "operation": "power",
            "a": 2,
            "b": 3
        }
    )

    assert response.status_code == 400


def test_api_divide_by_zero():
    client = app.test_client()

    response = client.post(
        "/calculate",
        json={
            "operation": "divide",
            "a": 10,
            "b": 0
        }
    )

    assert response.status_code == 400

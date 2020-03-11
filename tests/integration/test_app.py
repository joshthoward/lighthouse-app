import json
import pytest
import requests


def test_health_check():
    response = requests.get("http://0.0.0.0:5000")
    assert response.status_code == 200
    assert response.json() == {"message": "healthy"}


def test_predict():
    payload = json.dumps({
        "data": [
            {
                "ts": "2020-01-01T00:00:00.000Z",
                "f2": 1.0,
                "f3": 0.5
            }
        ]
    })

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post("http://0.0.0.0:5000/predict", payload,
                             headers=headers)
    assert response.status_code == 200


def test_score():
    payload = json.dumps({
        "data": [
            {
                "ts": "2020-01-01T00:00:00.000Z",
                "f1": 1.0,
                "f2": 1.0,
                "f3": 0.5
            }
        ]
    })

    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post("http://0.0.0.0:5000/score", payload,
                             headers=headers)
    assert response.status_code == 200


def test_update():
    payload = json.dumps({
        "data": [
            {
                "ts": "2020-01-01T00:00:00.000Z",
                "f1": 1.0,
                "f2": 1.0,
                "f3": 0.5
            }
        ]
    })

    headers = {
        "Content-Type": "application/json",
    }
    response = requests.put("http://0.0.0.0:5000/update", payload,
                             headers=headers)
    assert response.status_code == 200

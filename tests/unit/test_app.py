import mock
import pytest

from app.__main__ import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "ok"}


@mock.patch("app.__main__.model")
def test_predict(mock_model, client):
    
    def predict(ts, exog=None):
        return {"f1": 0.0}

    mock_model.predict.side_effect = predict

    json = {
        "data": [
            {
                "ts": "2020-01-01",
                "exog": {"f2": 1}
            }
        ]
    }

    response = client.post("/predict", json=json)
    assert response.status_code == 200
    assert response.json == [{"f1": 0.0}]
    mock_model.predict.assert_called_once_with("2020-01-01", {"f2": 1})


@mock.patch("app.__main__.model")
def test_score(mock_model, client):
    
    def score(ts, endog, exog=None):
        return {"f1": 0.0}

    mock_model.score.side_effect = score

    json = {
        "data": [
            {
                "ts": "2020-01-01",
                "endog": {"f1": 0.0},
                "exog": {"f2": 1}
            }
        ]
    }

    response = client.post("/score", json=json)
    assert response.status_code == 200
    assert response.json == [{"f1": 0.0}]
    mock_model.score.assert_called_once_with("2020-01-01", {"f1": 0.0}, {"f2": 1})


@mock.patch("app.__main__.model")
def test_update(mock_model, client):
    
    def update(ts, endog, exog=None):
        pass

    mock_model.update.side_effect = update

    json = {
        "data": [
            {
                "ts": "2020-01-01",
                "endog": {"f1": 0.0},
                "exog": {"f2": 1}
            }
        ]
    }

    response = client.put("/update", json=json)
    assert response.status_code == 200
    assert response.json == {"message": "ok"}
    mock_model.update.assert_called_once_with("2020-01-01", {"f1": 0.0}, {"f2": 1})

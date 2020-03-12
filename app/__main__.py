import pickle
import sys

from flask import Flask, jsonify, request


app = Flask(__name__)

model = None


@app.route("/")
def health_check():
    return jsonify({"message": "ok"})


@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()
    request_data = payload.get("data")
    response = [model.predict(d.get("ts"), d.get("exog"))
                for d in request_data]
    return jsonify(response)


@app.route("/score", methods=["POST"])
def score():
    payload = request.get_json()
    request_data = payload.get("data")
    response = [model.score(d.get("ts"), d.get("endog"), d.get("exog"))
                for d in request_data]
    return jsonify(response)


@app.route("/update", methods=["PUT"])
def update():
    payload = request.get_json()
    request_data = payload.get("data")
    updates = [model.update(d.get("ts"), d.get("endog"), d.get("exog"))
               for d in request_data]
    return jsonify({"message": "ok"})


def main():

    try:
        model_path = sys.argv[1]
        with open(model_path, "rb") as f:
            model = pickle.load(f)

    except IndexError:
        pass

    app.run(host="0.0.0.0", debug=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())

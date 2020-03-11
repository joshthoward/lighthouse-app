import pickle
import sys

from flask import Flask, jsonify, request


app = Flask(__name__)

model = None


@app.route("/")
def health_check():
    return jsonify({"message": "healthy"})


@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()
    request_data = payload.get("data")
    response = {}
    return jsonify(response)


@app.route("/score", methods=["POST"])
def score():
    payload = request.get_json()
    response = {}
    return jsonify(response)


@app.route("/update", methods=["PUT"])
def update():
    payload = request.get_json()
    response = {}
    return jsonify(response)


def main():

    try:
        model_path = sys.argv[1]
    except IndexError:
        return 1

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    app.run(host="0.0.0.0", debug=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())

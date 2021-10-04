from typing import Tuple
from http import HTTPStatus

import joblib
import pandas as pd
from flask import Flask, request, jsonify, Response

from utils import Preprocessor

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """Home endpoint"""
    html = """
    <h1>Sentiment Classifier</h1>
    <p>Endpoint: '/classify'</p>
    <p>method: 'POST'</p>
    <p>example request body: {"text": "I love python"}</p>
    """
    return html


@app.route("/classify", methods=["POST"])
def classify() -> Tuple[Response, int]:
    """Endpoint for sentiment classification task"""
    if not request.json:
        error_message = {"error": {"details": "POST request body is invalid."}}
        return jsonify(error_message), HTTPStatus.BAD_REQUEST

    text = request.json.get("text")
    if not text:
        error_message = {"error": {"details": "Parameter 'text' is missing."}}
        return jsonify(error_message), HTTPStatus.BAD_REQUEST

    if not isinstance(text, str):
        error_message = {"error": {"details": "Parameter 'text' isn't string."}}
        return jsonify(error_message), HTTPStatus.BAD_REQUEST

    pipeline = joblib.load("./model/pipeline.pkl")
    [prediction] = pipeline.predict(pd.Series(text))

    sentiment = "positive" if prediction else "negative"

    return jsonify({"text": text, "sentiment": sentiment}), HTTPStatus.OK


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

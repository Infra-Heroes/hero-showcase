import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Hello from NanoStack Showcase!",
        "feature": "secrets",
        "env": dict(os.environ)
    })

@app.route('/health')
def health():
    return "OK", 200


@app.route('/secrets')
def get_secrets():
    return jsonify({
        "API_KEY_PRESENT": "API_KEY" in os.environ,
        "DB_PASS_PRESENT": "DB_PASS" in os.environ
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

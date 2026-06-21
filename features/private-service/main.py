import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Hello from NanoStack Showcase!",
        "feature": "private-service",
        "env": dict(os.environ)
    })

@app.route('/health')
def health():
    return "OK", 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

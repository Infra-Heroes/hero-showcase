import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "message": "Hello from NanoStack Showcase!",
        "feature": "volumes",
        "env": dict(os.environ)
    })

@app.route('/health')
def health():
    return "OK", 200


@app.route('/data')
def read_data():
    try:
        with open('/app/data/test.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found. Try writing to it first!", 404

@app.route('/data/<content>', methods=['POST'])
def write_data(content):
    os.makedirs('/app/data', exist_ok=True)
    with open('/app/data/test.txt', 'w') as f:
        f.write(content)
    return "Data written successfully to persistent volume!", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    # Simulate a lightweight handler that returns JSON
    return jsonify({
        "status": "ok",
        "message": "Benchmark target active",
        "timestamp": time.time()
    })

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/healthz')
def healthz():
    return "OK", 200

@app.route('/')
def hello():
    log_level = os.environ.get('LOG_LEVEL', 'INFO')
    return f"Hello from Python Flask! (Log Level: {log_level})"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

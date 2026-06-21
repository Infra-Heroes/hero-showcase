from flask import Flask, render_template_string
import os
import time
import threading

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html>
<head><title>Autoscaling Demo</title></head>
<body>
    <h1>NanoStack Autoscaling Demo</h1>
    <p>Use the endpoint below to artificially spike CPU usage and trigger NanoStack's auto-scaler!</p>
    <form action="/stress" method="POST">
        <button type="submit" style="padding:10px 20px; font-size: 16px; background: red; color: white;">🔥 Spike CPU for 10 seconds 🔥</button>
    </form>
</body>
</html>
'''

def stress_cpu(duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        _ = 2 ** 20  # Busy wait

@app.route('/')
def index():
    return render_template_string(template)

@app.route('/stress', methods=['POST'])
def stress():
    threading.Thread(target=stress_cpu, args=(10,)).start()
    return "CPU spike started in background for 10 seconds! Keep an eye on your replica count.", 202

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

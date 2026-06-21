from flask import Flask, render_template_string
import time

# Simulate a heavy 3-second cold start when the container boots!
print("Starting heavy initialization...")
time.sleep(3)
print("Initialization complete!")

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html>
<head><title>Scale-to-Zero Demo</title></head>
<body>
    <h1>NanoStack Scale-to-Zero Demo</h1>
    <p>This app takes 3 seconds to boot. If you let it scale to zero by being idle, the next request will experience a 3-second cold start latency. That proves it scaled down and back up!</p>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(template)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

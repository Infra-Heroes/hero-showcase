from flask import Flask, request, render_template_string
import os

app = Flask(__name__)
DATA_FILE = '/app/data/test.txt'

template = '''
<!DOCTYPE html>
<html>
<head><title>Volumes Demo</title></head>
<body>
    <h1>NanoStack Volumes Demo</h1>
    <p>This demonstrates writing to a persistent volume mounted at <code>/app/data</code>.</p>
    <form method="POST">
        <input type="text" name="content" placeholder="Enter message to save..." required>
        <button type="submit">Save</button>
    </form>
    <h3>Current File Content:</h3>
    <pre style="background:#eee;padding:10px;">{{ content }}</pre>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        os.makedirs('/app/data', exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            f.write(request.form['content'])
            
    content = "File not found or empty."
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            content = f.read()
            
    return render_template_string(template, content=content)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

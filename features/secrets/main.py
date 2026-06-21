from flask import Flask, render_template_string
import os

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html>
<head><title>Secrets Demo</title></head>
<body>
    <h1>NanoStack Secrets Demo</h1>
    <p>This checks if secrets are properly injected by NanoStack or if they are still raw "secret:KEY" strings.</p>
    <div style="padding: 20px; border: 2px solid {{ 'green' if unlocked else 'red' }};">
        <h2>Vault Status: {{ 'UNLOCKED 🔓' if unlocked else 'LOCKED 🔒' }}</h2>
        <ul>
            <li><b>API_KEY:</b> {{ api_key }}</li>
            <li><b>DB_PASS:</b> {{ db_pass }}</li>
        </ul>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    api_key = os.environ.get('API_KEY', 'NOT_SET')
    db_pass = os.environ.get('DB_PASS', 'NOT_SET')
    
    # If they equal the exact raw string, they weren't resolved.
    unlocked = (api_key != 'secret:API_KEY' and api_key != 'NOT_SET') and (db_pass != 'secret:DB_PASS' and db_pass != 'NOT_SET')
    
    return render_template_string(template, api_key=api_key, db_pass=db_pass, unlocked=unlocked)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

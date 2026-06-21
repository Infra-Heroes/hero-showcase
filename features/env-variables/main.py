from flask import Flask, render_template_string
import os

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html>
<head><title>Env Vars Demo</title></head>
<body>
    <h1>Infra-Heroes Env Vars Demo</h1>
    <p>The following environment variables were injected from <code>hero.toml</code>:</p>
    <table border="1" cellpadding="5">
        <tr><th>Key</th><th>Value</th></tr>
        {% for k, v in env.items() %}
        <tr><td>{{ k }}</td><td>{{ v }}</td></tr>
        {% end endfor %}
    </table>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(template.replace('endfor', 'for'), env=dict(os.environ))

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

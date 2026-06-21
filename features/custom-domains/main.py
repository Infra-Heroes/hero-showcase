from flask import Flask, request, render_template_string

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html>
<head><title>Custom Domains Demo</title></head>
<body>
    <h1>Infra-Heroes Custom Domains Demo</h1>
    <p>This demonstrates routing via custom CNAMEs.</p>
    <h3>You accessed this service via: <span style="color: blue;">{{ host }}</span></h3>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(template, host=request.host)

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

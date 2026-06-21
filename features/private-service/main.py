from flask import Flask, request, render_template_string

app = Flask(__name__)

template = '''
<!DOCTYPE html>
<html>
<head><title>Private Service Demo</title></head>
<body>
    <h1>Infra-Heroes Private Service Demo</h1>
    <p>This service is marked as <code>private = true</code>. It shouldn't be accessible via the public load balancer.</p>
    <h3>Your Connection Details:</h3>
    <ul>
        <li><b>Remote IP:</b> {{ remote_addr }}</li>
        <li><b>X-Forwarded-For:</b> {{ forwarded }}</li>
    </ul>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(template, 
                                remote_addr=request.remote_addr, 
                                forwarded=request.headers.get('X-Forwarded-For', 'None'))

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

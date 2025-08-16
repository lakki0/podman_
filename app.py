from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Root route
@app.route('/')
def hello():
    return 'Hello from Flask running in Podman!'

# New: current server time
@app.route('/time')
def get_time():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'Current server time: {now}'

# New: dynamic greeting
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name.capitalize()}! Welcome to the Flask app in Podman.'

# New: JSON health check/status
@app.route('/status')
def status():
    return jsonify({
        'status': 'ok',
        'message': 'Flask app is running inside Podman',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


from flask import Flask, render_template, request, jsonify
import webbrowser
import threading

app = Flask(__name__)

# Store messages as dictionaries to include user names
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    username = request.form['username']
    message = request.form['message']
    messages.append({'user': username, 'message': message})
    return jsonify(messages)

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    app.run(debug=True)
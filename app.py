from flask import flask
app = Flask(__name__)

@app.route('/')
def hello world ():
    return "Hello. Welcome to my First Python DevOps Project"

@app.route('/health')
def health:
    return 'Server is Up and Running'

# Import Dependencies
from flask import Flask

# Create a new Flask app instance
app = Flask(__name__)

# Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello')
def hello():
    return '<h1>A Big Hello!!</h1>'

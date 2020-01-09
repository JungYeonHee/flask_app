from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello. World!'

@app.route('/')
def index():
   return 'Index Page'

@app.route('/hell0')
def hello():
    return 'Hello, World'
from flask import Flask, request, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/simpson/')
def simpson():
    pass

@app.route('/trapecio/')
def trapecio():
    pass

@app.route('/')
def index():
    pass
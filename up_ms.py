from flask import Flask, request, render_template
from flask_restful import Resource, Api
from Services.SimpsonRule import SimpsonRule
from Services.TrapecioRule import TrapecioRule

app = Flask(__name__)
api = Api(app)

# http://localhost:2511/
@app.route('/simpson/<a>/<b>/<exp>/<n>/<h>')
def simpson(a, b, exp, n, h):
    return SimpsonRule().get_integral(
        a, b, exp, n, h
    )

@app.route('/trapecio/<a>/<b>/<exp>/<n>/<h>')
def trapecio(a, b, exp, n, h):
    return TrapecioRule().get_integral(
        a, b, exp, n, h
    )

@app.route('/')
def index():
    return render_template('information.html')


if __name__ == '__main__':
    app.run(port=2511)
    
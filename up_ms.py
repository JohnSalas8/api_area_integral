from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api
from Services.SimpsonRule import SimpsonRule
from Services.TrapecioRule import TrapecioRule

app = Flask(__name__)
api = Api(app)

# http://localhost:2511/simpson/1/3/x**3-x+1/None/0.5
@app.route('/simpson/<a>/<b>/<exp>/<n>/<h>')
def simpson(a, b, exp, n, h):
    if n=='None':
        return jsonify(
            SimpsonRule().get_integral(
                float(a), float(b), exp, None, float(h)
            )
        )
    if h=='None':
        return jsonify(
            SimpsonRule().get_integral(
                float(a), float(b), exp, int(n), None
            )
        )
    
    return ''

# http://localhost:2511/trapecio/1/3/x**3-x+1/None/0.5
@app.route('/trapecio/<a>/<b>/<exp>/<n>/<h>')
def trapecio(a, b, exp, n, h):
    if n=='None':
        return jsonify(
            TrapecioRule().get_integral(
                float(a), float(b), exp, None, float(h)
            )
        )
    if h=='None':
        return jsonify(
            TrapecioRule().get_integral(
                float(a), float(b), exp, int(n), None
            )
        )
    
    return ''

@app.route('/')
def index():
    return render_template('information.html')


if __name__ == '__main__':
    app.run(port=2511)
    
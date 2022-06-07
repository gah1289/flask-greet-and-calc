# Put your app in here.
from operations import add,sub,mult,div

from flask import Flask, request
app = Flask(__name__)



@app.route('/add')
def addition():
    a=request.args['a']
    b=request.args['b']
    return str(add(int(a),int(b)))


@app.route('/sub')
def subtract():
    a=request.args['a']
    b=request.args['b']
    return str(sub(int(a),int(b)))

@app.route('/mult')
def multiply():
    a=request.args['a']
    b=request.args['b']
    return str(mult(int(a),int(b)))

@app.route('/div')
def divide():
    a=request.args['a']
    b=request.args['b']
    return str(div(int(a),int(b)))



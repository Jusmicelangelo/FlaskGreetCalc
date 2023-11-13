from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def getback_add():
    """"Getting back an addition of a and b""" 
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)

@app.route("/subtract")
def getback_subtract():
    """"Getting back an addition of a and b""" 
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)

@app.route("/multiply")
def getback_multiply():
    """"Getting back an addition of a and b""" 
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)

@app.route("/divide")
def getback_divide():
    """"Getting back an addition of a and b""" 
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)

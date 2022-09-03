from flask import Flask, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

import operations

@app.route('/add')
def add_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    sum = str(operations.add(a,b))
    return sum

@app.route('/sub')
def sub_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    sub = str(operations.sub(a,b))
    return sub

@app.route('/mult')
def mult_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    mult = str(operations.mult(a,b))
    return mult

@app.route('/div')
def div_nums():
    a = int(request.args["a"])
    b = int(request.args["b"])
    div = str(operations.div(a,b))
    return div

# operators = {
#         "add": add,
#         "sub": sub,
#         "mult": mult,
#         "div": div,
#         }

# @app.route("/math/<oper>")
# def do_math(oper):
#     """Do math on a and b."""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)

#     return str(result)
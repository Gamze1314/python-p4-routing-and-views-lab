#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():  # index view 
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route("/print/<string:parameter>")  # <converter:variable_name>
def print_string(parameter):
    print(parameter) # Prints to console.
    return parameter


# display all numbers in the range of the parameter on separate lines.
@app.route('/count/<int:param>')
def count(param):
    result = "" # expected output is a string.
    for i in range(param): # display numbers until param
        result += f"{i}\n" # update result.
    return result


@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Cannot divide by zero", 400
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400

    return str(result)



if __name__ == '__main__':
    app.run(port=5555, debug=True)

#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string (parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for num in range(parameter):

        result += str(num) + '\n'
    return result

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operation == "+":
       return str(num1 + num2 )
    # A math() view should take three parameters: num1,
    #  operation, and num2. It must perform the appropriate 
    # operation on the two numbers in the order that they are 
    # presented. The included operations should be: +, -, *, div 
    # (/ would change the URL path), and %. Its URL should be of 
    # the format /math/<num1>/<operation>/<num2>.
    elif operation == "-":
        return str(num1 - num2) 
    elif operation == "*":
        return str(num1 * num2) 
    elif operation == "div":
        return str(num1 / num2) 
    elif operation == "%":
        return str(num1 % num2) 
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)


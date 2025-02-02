#!/usr/bin/python3
""" script that starts a Flask web application """


from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello():
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    return ('HBNB')


@app.route('/c/<text>')
def c_handler(text):
    new_text = text.replace("_", " ")
    return ('C ' + new_text)


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_handler(text):
    new_text = text.replace("_", " ")
    return ('Python ' + new_text)


@app.route('/number/<int:n>')
def integer_handler(n):
    return (str(n) + ' is a number')


@app.route('/number_template/<int:n>')
def integer_template_handler(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even_template_handler(n=None):
    if n % 2 == 0:
        odd = 'even'
    else:
        odd = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, odd=odd)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)

#!/usr/bin/python3
""" script that starts a Flask web application """


from flask import Flask
app = Flask(__name__)
app.strict_slashes=False

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)

#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template

# create an instance of Flask
app = Flask(__name__)


# map root /
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


# map root /hbnb
@app.route("/hbnb", strict_slashes=False)
def _hbnb():
    return "HBNB"


# map to c
@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)


# Map /python/<text>
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    spaced_text = text.replace('_', ' ')
    return 'Python {}'.format(spaced_text)


# Map /number/<n>
@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Function that displays "<passed number>"""
    return '{} is a number'.format(n)


# Map /number_template/<n>
@app.route('/number_template/<int:n>')
def number_template_route(n):
    """Function to display an HTML page if n is an integer"""
    return (render_template('5-number.html', n=n))


# Map /number_odd_or_even/<n>
@app.route('/number_odd_or_even/<int:n>')
def odd_or_even_route(n):
    '''Function to display an HTML page if n is an integer.'''
    return(render_template('6-number_odd_or_even.html', n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

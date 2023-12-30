#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

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

#map to c
@app.route("/c/<text>", strict_slashes=False)
def c_route():
    """Displays 'C' followed by the value of <text>."""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

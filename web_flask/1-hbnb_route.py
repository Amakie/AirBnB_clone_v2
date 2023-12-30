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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

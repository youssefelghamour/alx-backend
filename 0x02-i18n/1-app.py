#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ flask babel config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
# takes the Config class and loads all attributes defined
# within it into the Flask application's configuration
app.config.from_object(Config)
# Babel inherits the above configs from the flask app
babel = Babel(app)


@app.route('/', strict_slashes=False)
def home():
    """ render index page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

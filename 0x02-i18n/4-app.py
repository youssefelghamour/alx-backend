#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template, request
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


# this decorator is equivalent to doing:
# babel = Babel(app, locale_selector=get_locale)
@babel.localeselector
def get_locale():
    """ determines the best match with our supported languages """
    ## Full request URL
    # full_url = request.url  # "http://127.0.0.1:5000/?locale=fr&name=ysf"

    ## URL path
    # path = request.path  # "/"

    ## URL parameters
    # args = request.args 
    # = ImmutableMultiDict([('locale', 'fr'), ('name', 'ysf')])
    # name = arg.get('name') # "ysf"

    # Check if 'locale' is in the request arguments and if it's valid
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def home():
    """ render index page """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

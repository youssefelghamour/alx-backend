#!/usr/bin/env python3
""" Basic flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz


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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ returns a user (dict) based on the id passed in:
        http://127.0.0.1:5000/?login_as=2
    """
    id = request.args.get('login_as')
    if id:
        return users[int(id)]
    return None


# decorator to make it be executed before all other functions
@app.before_request
def before_request():
    """ Fetches the user using get_user and sets it in flask.g.user
        mocks user authentification
    """
    # g.user is global and will be accessible in 5-index.html jinja template
    g.user = get_user()


# this decorator is equivalent to doing:
# babel = Babel(app, locale_selector=get_locale)
@babel.localeselector
def get_locale():
    """ determines the best match with our supported languages """
    # Check if 'locale' is in the request arguments and if it's valid
    if 'locale' in request.args:
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale

    # Check if there is a logged-in user and use their preferred locale
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    # fallback to accepting languages based on client preferences
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_timezone():
    """ returns timezone from URL or user settings, defaults to UTC """
    timezone = request.args.get('timezone', '').strip()
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user:
        timezone = g.user.get('timezone')
        if timezone:
            try:
                pytz.timezone(timezone)
                return timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def home():
    """ render index page """
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

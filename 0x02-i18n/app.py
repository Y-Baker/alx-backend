#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template, request, g
import pytz
from config_babel import Config
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(Config)


def get_locale() -> str:
    """ Get locale """
    langs = request.args.get('locale', '')[1:-1].split('|')
    for lang in langs:
        if lang in app.config['LANGUAGES']:
            return lang
    user = g.user
    if user and user.locale in app.config['LANGUAGES']:
        return user.locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Get user """
    from config_babel import users
    id = request.args.get('login_as', None)
    if id:
        id = int(id)
        return users.get(id, None)
    return None


@app.before_request
def before_request() -> None:
    """ Before request """
    from flask import g
    g.user = get_user()
    g.time = get_timezone()
    print(g.time)


def get_timezone() -> str:
    """ Get timezone """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user.get('timezone', '')

    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale,
               timezone_selector=get_timezone)


@app.route('/')
def home():
    """ Home page """
    return render_template('index.html')

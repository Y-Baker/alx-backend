#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template, request
from config_babel import Config
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """ Get locale """
    langs = request.args.get('locale', '')[1:-1].split('|')
    for lang in langs:
        if lang in app.config['LANGUAGES']:
            return lang
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
def before_request():
    """ Before request """
    from flask import g
    g.user = get_user()


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    """ Home page """
    return render_template('5-index.html')

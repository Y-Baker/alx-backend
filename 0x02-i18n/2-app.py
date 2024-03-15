#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template, request
from config_babel import Config
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """ Get locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home():
    """ Home page """
    return render_template('2-index.html')

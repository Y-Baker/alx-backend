#!/usr/bin/env python3
""" Basic Babel setup """

from config_babel import Config
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def home():
    """ Home page """
    return render_template('1-index.html')

#!/usr/bin/env python3
""" Basic Babel setup """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """ Home page """
    return render_template('0-index.html')

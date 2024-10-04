#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/hello')
def hello():
    return "Hello from the /hello route!"

@app.route('/about')
def about():
    return "This is the About page. We are learning Flask!"

@app.route('/contact')
def contact():
    return "Contact us at example@example.com!"

if __name__ == '__main__':
    app.run(debug=True)


	
#!/usr/bin/env python3

import os

from flask import Flask, render_template

from stock import Stock


app = Flask(
    __name__,
    static_folder='./static/',
    static_url_path='',
    template_folder='./templates/')


@app.route('/')
def index():
    stocks = Stock()
    s = stocks.get_stocks()
    if s is None:
        s = {"-": {}}
    return render_template('index.html', stocks=s)


def get_PORT() -> int:
    PORT = os.getenv('PORT')
    if PORT is None:
        raise Exception('PORT is None')
    elif not PORT.isdecimal():
        raise Exception('Could not convert port to int')
    return int(PORT)


def get_DEBUG() -> bool:
    DEBUG = os.getenv('DEBUG')
    if DEBUG is None:
        return False
    return DEBUG.lower() == 'true'


def get_env() -> dict:
    env = {}
    env['PORT'] = get_PORT()
    env['DEBUG'] = get_DEBUG()
    return env


def add_env():  # TODO: del
    os.environ["PORT"] = "3031"
    os.environ["DEBUG"] = "true"
    os.environ["SERVICE_ACCOUNT_FILE"] = "kokomatu-571c685bf3c2.json"
    os.environ["SHEET_URL"] = "https://docs.google.com/spreadsheets/d/1_WIPIceaH-zv8zuzLSALYFMZ41qMHD9qKWIWj5sbXKg/edit"
    os.environ["WORKSHEET_NAME"] = "Sheet1"


if __name__ == '__main__':
    env = get_env()
    print(f"{env['PORT']}")
    print(f"{env['DEBUG']}")
    app.run(port=env['PORT'], debug=env['DEBUG'])

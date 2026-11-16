# -*- coding: utf-8 -*-
"""Local dev runner (Flask-Script is replaced by the built-in Flask CLI)."""

from application import create_app

app = create_app('default')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7345)
# -*- coding: utf-8 -*-
"""WSGI entry point: gunicorn wsgi:app / flask --app wsgi run"""

from application import create_app

app = create_app('default')
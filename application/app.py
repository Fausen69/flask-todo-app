# -*- coding: utf-8 -*-

import click
from flask import Flask

from .controllers import blueprints
from .configs import config
from .extensions import db, migrate


def create_app(config_name=None):
    if config_name is None:
        config_name = 'default'

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    for bp in blueprints:
        app.register_blueprint(bp)

    register_commands(app)
    return app


def register_commands(app):
    @app.cli.command("init-db")
    @click.option("--seed", is_flag=True, help="Insert a demo task")
    def init_db(seed):
        """Create SQLite schema (and optional demo data)."""
        from .models import Todo

        db.create_all()
        if seed and Todo.query.count() == 0:
            Todo(title="task created by CI").store_to_db()
        click.echo("Database initialised: %s" % app.config["SQLALCHEMY_DATABASE_URI"])
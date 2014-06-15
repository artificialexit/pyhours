from flask import Flask, render_template
from importlib import import_module
import models


def register_plugins(app):
    plugins = import_module('.plugins', __package__)
    [item.init_app(app)
     for item in vars(plugins).values()
     if not type(item) == type and hasattr(item, 'init_app')]


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_plugins(app)

    @app.context_processor
    def inject_layout():
        return dict(layout='layout.html')

    @app.route("/")
    def index():
        return render_template('index.html')

    return app

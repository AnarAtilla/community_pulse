from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to Community Pulse API!"}), 200

    from .routers.questions import questions
    from .routers.responses import responses_bp

    app.register_blueprint(questions)
    app.register_blueprint(responses_bp, url_prefix='/api')

    return app
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

    from app.routers.questions import questions_bp
    from app.routers.responses import responses_bp

    app.register_blueprint(questions_bp)
    app.register_blueprint(responses_bp, url_prefix='/api')

    # Ensure models are imported
    from app.models import Category, Question, Response

    return app
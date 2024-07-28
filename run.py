from app import create_app, db
from flask_migrate import Migrate, upgrade
from app.routers.responses import responses_bp

app = create_app()
migrate = Migrate(app, db)

# Register the blueprint with the correct prefix
if not any(bp.name == responses_bp.name for bp in app.blueprints.values()):
    app.register_blueprint(responses_bp, url_prefix='/api')


@app.cli.command("db_init")
def db_init():
    """Initialize the database."""
    upgrade()


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from .extensions import db  # Импортируем db из extensions
from flask_migrate import Migrate

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_delivery.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import bp, bp_admin
    from .auth_routes import bp_auth  # Импортируем bp_auth из auth_routes

    app.register_blueprint(bp, url_prefix='/')  # Регистрируем основной Blueprint
    app.register_blueprint(bp_admin, url_prefix='/admin')  # Регистрируем админ Blueprint
    app.register_blueprint(bp_auth, url_prefix='/auth')  # Регистрируем Blueprint для аутентификации

    return app

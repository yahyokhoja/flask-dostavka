
# app/__init__.py
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import Dish
from .extensions import db
from flask_migrate import Migrate
from .auth_routes import bp_auth  # Импортируем Blueprint для аутентификации
from .admin_routes import bp_admin  # Импортируем Blueprint для админки
from .auth_routes import bp_auth  # Импортируем Blueprint для аутентификации

# Инициализация Migrate
migrate = Migrate()

def create_app():
    # Создание экземпляра приложения
    app = Flask(__name__)

    # Конфигурация приложения
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_delivery.db'  # Замените путь на ваш
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'gjhgkjhdfsuytf87654hnuyfgdughjh'  # Замените на свой секретный ключ

    # Инициализация db
    db.init_app(app)
    
    # Инициализация миграций
    migrate.init_app(app, db)

    # Инициализация Flask-Admin
    admin = Admin(app, name='Food Delivery Admin', template_mode='bootstrap3')

    # Добавление модели Dish в админку
    admin.add_view(ModelView(Dish, db.session))

    # Регистрируем блюпринты# Blueprint для аутентификации
    app.register_blueprint(bp_auth, url_prefix='/auth')
     
    app.register_blueprint(bp_admin, url_prefix='/admin')  # Blueprint для админки

    # Если у вас есть основной Blueprint
    from .routes import bp
    app.register_blueprint(bp, url_prefix='/')

    return app

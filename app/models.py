from .extensions import db  # Импортируем db из extensions
from werkzeug.security import generate_password_hash, check_password_hash

# Модель для блюд
class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Dish {self.name}>'

# Модель для пользователей
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.String(15), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Метод для установки пароля (хэширование пароля)"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Метод для проверки пароля"""
        return check_password_hash(self.password_hash, password)

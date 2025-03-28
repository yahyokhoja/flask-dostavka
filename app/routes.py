from flask import Blueprint, render_template
from .models import Dish  # Импортируем модели

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    try:
        dishes = Dish.query.all()  # Получаем все блюда из базы данных
        return render_template('index.html', dishes=dishes)
    except Exception as e:
        return f"Произошла ошибка: {e}"
    






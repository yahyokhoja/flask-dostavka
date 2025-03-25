# app/admin_routes.py
from flask import Blueprint, render_template

# Создаем Blueprint для админки
bp_admin = Blueprint('admin', __name__)

# Маршрут для главной страницы админки (например, дашборд)
@bp_admin.route('/dashboard')
def dashboard():
    return render_template('admin_dashboard.html')  # Шаблон для дашборда админки

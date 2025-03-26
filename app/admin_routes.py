from flask import Blueprint, render_template
bp_admin = Blueprint('admin_routes', __name__, url_prefix='/admin')


@bp_admin.route('/dashboard')
def dashboard():
    return render_template('admin_dashboard.html')

@bp_admin.route('/add_dish')
def add_dish():
    return "Добавление блюда"

@bp_admin.route('/view_dishes')
def view_dishes():
    return "Просмотр блюд"

@bp_admin.route('/view_users')
def view_users():
    return "Просмотр пользователей"

@bp_admin.route('/view_orders')
def view_orders():
    return "Просмотр заказов"

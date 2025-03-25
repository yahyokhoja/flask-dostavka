from flask import Blueprint, render_template, request, redirect, url_for

bp_auth = Blueprint('auth', __name__)

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Логика для обработки входа
        return redirect(url_for('main.index'))
    return render_template('login.html')

@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Логика для регистрации нового пользователя
        return redirect(url_for('main.index'))
    return render_template('register.html')

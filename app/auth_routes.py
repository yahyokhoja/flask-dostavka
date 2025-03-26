# app/auth_routes.py
from flask import Blueprint, render_template, flash, redirect, url_for
from .forms import RegisterForm
from .models import User  # Модели пользователей, если необходимо

bp_auth = Blueprint('auth_routes', __name__)

@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Логика регистрации пользователя
        flash('Вы успешно зарегистрировались!', 'success')
        return redirect(url_for('auth_routes.login'))  # Исправлено на 'auth_routes.login'

    return render_template('register.html', form=form)

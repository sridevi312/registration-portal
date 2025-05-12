from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User
from werkzeug.security import generate_password_hash

# Create Blueprint
main = Blueprint('main', __name__)

# Home Route (Redirect to Login)
@main.route('/')
def home():
    return redirect(url_for('main.login'))

# Registration Route
@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or email already exists. Please try another one.', 'danger')
            return redirect(url_for('main.register'))

        # Create a new user with the given username, email, and hashed password
        new_user = User(username=username, email=email)
        new_user.set_password(password)

        # Add user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')

# Login Route
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Find user by email
        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):  # Check password with hashed password
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
            return redirect(url_for('main.login'))

    return render_template('login.html')

# Dashboard Route (Protected Page)
@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

# Logout Route
@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('main.login'))

# Dummy Payment Route (To simulate payment, in a real scenario you'd integrate Razorpay)
@main.route('/pay')
@login_required
def pay():
    # Update user's payment status
    current_user.payment_status = 'Paid'
    db.session.commit()
    flash('Payment successful (dummy).', 'success')
    return redirect(url_for('main.dashboard'))

from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required, flash
from flask_sqlalchemy import SQLAlchemy
from .models import User, Base
from helpers import check_username_exists
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
login_manager = LoginManager()
app.secret_key = os.getenv("SECRET_KEY")
login_manager.init_app(app)
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mindtrack.db"
db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')


        if password != confirm_password:
            flash('Passwords do not match')
            return render_template('register.html')
        
        if check_username_exists(username=username):
            flash('This user already exists, please log in')
            return redirect(url_for('login'))
        
        else:
            new_user = User(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Placeholder for login logic
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():

    #logout_user()
    render_template('index.html')


@login_required
@app.route('/profile', methods=['POST'])
def create_profile():
    # Placeholder for profile creation
    return jsonify({"status": "Profile created"})


@app.route('/questionnaire', methods=['POST'])
@login_required
def generate_plan():
    # Placeholder for questionnaire logic
    return jsonify({"plan": "Generated plan based on answers"})

if __name__ == '__main__':
    app.run(debug=True)
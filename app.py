from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from models import User, JournalEntry, QuestionnaireResponse
from helpers import check_username_exists
import os
import json
from datetime import datetime, date, timedelta
from dotenv import load_dotenv
from database import db
load_dotenv()


app = Flask(__name__)
login_manager = LoginManager()
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mindtrack.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
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
            return redirect(url_for('register'))
        
        if check_username_exists(username=username):
            flash('This user already exists, please log in')
            return redirect(url_for('login'))
        
        
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully')
    return redirect(url_for('index'))


@login_required
@app.route('/profile', methods=['GET','POST'])
def create_profile():
    # Placeholder for profile creation
    return jsonify({"status": "Profile created"})


@app.route('/dashboard')
@login_required
def dashboard():
    # Get recent journal entries and questionnaire responses
    recent_entries = JournalEntry.query.filter_by(user_id=current_user.id).order_by(JournalEntry.created_at.desc()).limit(5).all()
    latest_response = QuestionnaireResponse.query.filter_by(user_id=current_user.id).order_by(QuestionnaireResponse.created_at.desc()).first()
    today = date.today()
    
    # Get data for charts (last 7 days)
    from datetime import timedelta
    week_ago = today - timedelta(days=7)
    
    # Mood data from journal entries
    mood_data = JournalEntry.query.filter(
        JournalEntry.user_id == current_user.id,
        JournalEntry.created_at >= week_ago
    ).order_by(JournalEntry.created_at.asc()).all()
    
    # Wellness data from questionnaire responses
    wellness_data = QuestionnaireResponse.query.filter(
        QuestionnaireResponse.user_id == current_user.id,
        QuestionnaireResponse.created_at >= week_ago
    ).order_by(QuestionnaireResponse.created_at.asc()).all()
    
    return render_template('dashboard.html', 
                         user=current_user, 
                         entries=recent_entries, 
                         latest_response=latest_response, 
                         today=today,
                         mood_data=mood_data,
                         wellness_data=wellness_data)

@app.route('/questionnaire', methods=['GET', 'POST'])
@login_required
def questionnaire():
    if request.method == 'POST':
        # Process questionnaire responses
        mood = request.form.get('mood')
        sleep_hours = float(request.form.get('sleep_hours', 0))
        exercise = request.form.get('exercise')
        stress_level = int(request.form.get('stress_level', 5))
        
        # Save the responses
        response = QuestionnaireResponse(
            user_id=current_user.id,
            mood=mood,
            sleep_hours=sleep_hours,
            exercise=exercise,
            stress_level=stress_level
        )
        db.session.add(response)
        db.session.commit()
        
        flash('Questionnaire completed! Your personalized plan has been generated.')
        return redirect(url_for('dashboard'))
    
    return render_template('questionnaire.html')

@app.route('/journal', methods=['GET', 'POST'])
@login_required
def journal():
    if request.method == 'POST':
        entry_text = request.form.get('entry')
        mood_rating = int(request.form.get('mood_rating', 5))
        
        # Save the journal entry
        entry = JournalEntry(
            user_id=current_user.id,
            content=entry_text,
            mood_rating=mood_rating
        )
        db.session.add(entry)
        db.session.commit()
        
        flash('Journal entry saved successfully!')
        return redirect(url_for('journal'))
    
    # Get recent entries for display
    entries = JournalEntry.query.filter_by(user_id=current_user.id).order_by(JournalEntry.created_at.desc()).limit(10).all()
    return render_template('journal.html', entries=entries)

@app.route('/analytics')
@login_required
def analytics():
    return render_template('analytics.html')

@app.route('/api/chart-data')
@login_required
def chart_data():
    # Get data for the last 30 days
    thirty_days_ago = date.today() - timedelta(days=30)
    
    # Mood data from journal entries
    mood_entries = JournalEntry.query.filter(
        JournalEntry.user_id == current_user.id,
        JournalEntry.created_at >= thirty_days_ago
    ).order_by(JournalEntry.created_at.asc()).all()
    
    # Wellness data from questionnaire responses
    wellness_entries = QuestionnaireResponse.query.filter(
        QuestionnaireResponse.user_id == current_user.id,
        QuestionnaireResponse.created_at >= thirty_days_ago
    ).order_by(QuestionnaireResponse.created_at.asc()).all()
    
    # Format data for charts
    mood_chart_data = {
        'labels': [entry.created_at.strftime('%m/%d') for entry in mood_entries],
        'data': [entry.mood_rating for entry in mood_entries]
    }
    
    stress_chart_data = {
        'labels': [entry.created_at.strftime('%m/%d') for entry in wellness_entries],
        'data': [entry.stress_level for entry in wellness_entries]
    }
    
    sleep_chart_data = {
        'labels': [entry.created_at.strftime('%m/%d') for entry in wellness_entries],
        'data': [entry.sleep_hours for entry in wellness_entries]
    }
    
    # Exercise distribution data
    exercise_counts = {'none': 0, 'light': 0, 'moderate': 0, 'intense': 0}
    for entry in wellness_entries:
        if entry.exercise in exercise_counts:
            exercise_counts[entry.exercise] += 1
    
    exercise_chart_data = {
        'labels': ['None', 'Light', 'Moderate', 'Intense'],
        'data': [exercise_counts['none'], exercise_counts['light'], 
                exercise_counts['moderate'], exercise_counts['intense']]
    }
    
    return jsonify({
        'mood': mood_chart_data,
        'stress': stress_chart_data,
        'sleep': sleep_chart_data,
        'exercise': exercise_chart_data
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'change-this-key-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mindtrack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# DATABASE MODELS


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    entries = db.relationship('Entry', backref='user', lazy=True, cascade='all, delete-orphan')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    mood = db.Column(db.Integer, nullable=False)  # 1-5
    activity = db.Column(db.Text, nullable=False)
    tasks = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        return {
            'id': self.id,
            'date': days[self.date.weekday()] if self.date.weekday() < 7 else 'Today',
            'full_date': self.date.strftime('%Y-%m-%d'),
            'mood': self.mood,
            'activity': self.activity,
            'tasks': self.tasks,
            'timestamp': self.date.strftime('%Y-%m-%d')
        }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# AUTHENTICATION ROUTES

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        data = request.json
        user = User.query.filter_by(email=data.get('email')).first()
        
        if user and user.check_password(data.get('password')):
            login_user(user, remember=True)
            return jsonify({'success': True})
        
        return jsonify({'success': False, 'message': 'Incorrect email or password'}), 401
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        data = request.json
        
        if User.query.filter_by(email=data.get('email')).first():
            return jsonify({'success': False, 'message': 'This email is already in use'}), 400
        
        if User.query.filter_by(username=data.get('username')).first():
            return jsonify({'success': False, 'message': 'This username is already taken'}), 400
        
        user = User(
            username=data.get('username'),
            email=data.get('email')
        )
        user.set_password(data.get('password'))
        
        db.session.add(user)
        db.session.commit()
        
        login_user(user, remember=True)
        return jsonify({'success': True})
    
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# MAIN ROUTES

@app.route('/')
@login_required
def index():
    return render_template('index.html', username=current_user.username)

@app.route('/api/entries', methods=['GET'])
@login_required
def get_entries():
    # Get entries from the last 7 days
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=6)
    
    entries = Entry.query.filter(
        Entry.user_id == current_user.id,
        Entry.date >= start_date,
        Entry.date <= end_date
    ).order_by(Entry.date).all()
    
    return jsonify([entry.to_dict() for entry in entries])

@app.route('/api/entries', methods=['POST'])
@login_required
def add_entry():
    data = request.json
    today = datetime.now().date()
    
    # Check if an entry already exists for today
    existing_entry = Entry.query.filter_by(
        user_id=current_user.id,
        date=today
    ).first()
    
    if existing_entry:
        # Update existing entry
        existing_entry.mood = data.get('mood', 3)
        existing_entry.activity = data.get('activity', '')
        existing_entry.tasks = data.get('tasks', 0)
        db.session.commit()
        return jsonify({'success': True, 'entry': existing_entry.to_dict()})
    
    # Create new entry
    entry = Entry(
        user_id=current_user.id,
        date=today,
        mood=data.get('mood', 3),
        activity=data.get('activity', ''),
        tasks=data.get('tasks', 0)
    )
    
    db.session.add(entry)
    db.session.commit()
    
    return jsonify({'success': True, 'entry': entry.to_dict()})

@app.route('/api/entries/<int:entry_id>', methods=['DELETE'])
@login_required
def delete_entry(entry_id):
    entry = Entry.query.filter_by(id=entry_id, user_id=current_user.id).first()
    
    if not entry:
        return jsonify({'success': False, 'message': 'Entry not found'}), 404
    
    db.session.delete(entry)
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/stats', methods=['GET'])
@login_required
def get_stats():
    # Current week statistics
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=6)
    
    current_week = Entry.query.filter(
        Entry.user_id == current_user.id,
        Entry.date >= start_date,
        Entry.date <= end_date
    ).all()
    
    # Previous week statistics
    prev_end = start_date - timedelta(days=1)
    prev_start = prev_end - timedelta(days=6)
    
    prev_week = Entry.query.filter(
        Entry.user_id == current_user.id,
        Entry.date >= prev_start,
        Entry.date <= prev_end
    ).all()
    
    current_tasks = sum(e.tasks for e in current_week)
    prev_tasks = sum(e.tasks for e in prev_week)
    tasks_increase = current_tasks - prev_tasks
    
    avg_mood = round(sum(e.mood for e in current_week) / len(current_week), 1) if current_week else 0
    
    return jsonify({
        'total_tasks': current_tasks,
        'avg_mood': avg_mood,
        'tasks_increase': tasks_increase
    })

@app.route('/api/history', methods=['GET'])
@login_required
def get_history():
    # Get all user entries
    entries = Entry.query.filter_by(user_id=current_user.id).order_by(Entry.date.desc()).limit(30).all()
    return jsonify([entry.to_dict() for entry in entries])


def init_db():
    with app.app_context():
        db.create_all()
        print(" Database initialized")

if __name__ == '__main__':
    init_db()
    app.run(debug=False, host='0.0.0.0', port=5000)
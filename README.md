# MindTrack Journal

**Youth Coders Hack 2025 Project**  
A fully functional web application designed to help young users track their productivity and mental well-being through personalized plans and daily journaling.

---

## 🧠 Project Goals

- Help users reflect on their daily habits and emotions
- Generate personalized action plans based on a questionnaire
- Visualize progress through simple dashboards
- Encourage positive routines and self-awareness

---

## ✨ Features

### 🔐 Authentication System
- User registration and login
- Secure password hashing
- Session management with Flask-Login

### 📊 Dashboard
- Personalized welcome page
- Recent journal entries overview
- Latest wellness questionnaire results
- Personalized recommendations based on user data

### 📝 Daily Questionnaire
- Track mood, sleep hours, exercise, and stress levels
- Interactive form with sliders and dropdowns
- Data persistence to database
- Automatic recommendation generation

### 📖 Journal System
- Write personal journal entries
- Rate daily mood (1-10 scale)
- View previous entries chronologically
- Clean, readable interface

### 📊 Analytics & Visualizations
- **Chart.js Integration** for data visualization
- **Mood Trends** - Line chart tracking mood over time
- **Stress Level Monitoring** - Visual stress pattern analysis
- **Sleep Pattern Analysis** - Bar chart of sleep hours
- **Exercise Distribution** - Donut chart of activity types
- **30-day data tracking** with interactive charts
- **Mini dashboard chart** for quick insights

### 🎨 Modern UI/UX
- Responsive design for all devices
- Modern gradient styling with glassmorphism effects
- Smooth animations and transitions
- Professional typography with Inter font
- Interactive Chart.js visualizations

---

## 🧱 Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Data Visualization**: Chart.js
- **Styling**: Custom CSS with modern design principles
- **Version Control**: Git + GitHub

---

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mindtrack-journal
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and set your SECRET_KEY
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the app**
   Open your browser and go to `http://127.0.0.1:5000`

---

## 📁 Project Structure

```
mindtrack-journal/
├── app.py                 # Main Flask application
├── models.py             # Database models (User, JournalEntry, QuestionnaireResponse)
├── database.py           # Database configuration
├── helpers.py            # Utility functions
├── base.py              # SQLAlchemy base class
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
├── static/
│   └── styles.css       # Modern CSS styling
├── templates/
│   ├── layout.html      # Base template
│   ├── index.html       # Homepage
│   ├── login.html       # Login page
│   ├── register.html    # Registration page
│   ├── dashboard.html   # User dashboard
│   ├── questionnaire.html # Daily wellness form
│   └── journal.html     # Journal interface
└── instance/
    └── mindtrack.db     # SQLite database (auto-generated)
```

---

## 🔧 Key Improvements Made

### Backend Enhancements
- ✅ Fixed authentication system with proper login/logout
- ✅ Added missing User.get() method for Flask-Login
- ✅ Implemented complete questionnaire processing
- ✅ Created journal entry system with mood tracking
- ✅ Added database models for data persistence
- ✅ Configured proper Flask-Login settings

### Frontend Improvements
- ✅ Complete UI overhaul with modern design
- ✅ Responsive grid layouts
- ✅ Interactive forms with real-time feedback
- ✅ Professional color scheme and typography
- ✅ Mobile-friendly responsive design

### New Features Added
- ✅ User dashboard with data visualization
- ✅ Personalized recommendations engine
- ✅ Journal entry system with mood tracking
- ✅ Interactive questionnaire with sliders
- ✅ Flash messaging system for user feedback

---

## 🎯 Usage Guide

1. **Register**: Create a new account on the registration page
2. **Login**: Sign in with your credentials
3. **Dashboard**: View your wellness overview and quick actions
4. **Questionnaire**: Complete daily wellness check-ins
5. **Journal**: Write about your thoughts and experiences
6. **Track Progress**: Monitor your wellness journey over time

---

## 👥 Team Roles

- **Sanya**: Auth, profile setup, questionnaire 
- **Nickolas**: JSON logic or AI integration
- **Khyshnert**: Backend structure, task logging, feedback engine 

---

## 🚀 Future Enhancements

- Data visualization charts and graphs
- Export journal entries to PDF
- Email reminders for daily check-ins
- Social features (optional sharing)
- Mobile app development
- Advanced AI-powered insights

---

## 📝 License

This project is part of Youth Coders Hack 2025.


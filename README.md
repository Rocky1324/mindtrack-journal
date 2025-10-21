# MentalTrack Prototype

**MentalTrack** is a productivity journal with mental health insights.  
This is a prototype built to explore tracking tasks, mood, and progress over time.

## Overview

- Users can log daily tasks and rate their mood on a 1–5 scale.  
- Data is stored in a database (SQLite) and visualized with charts.  
- Weekly summaries are generated to provide insights like:
  - “You completed more tasks than last week”
  - “Your mood improved on days with outdoor activities”

This prototype was initially developed in French for personal testing and has been adapted to English for team collaboration.

## Features

- Daily task and mood logging  
- Visualization of task completion and mood over time (Chart.js)  
- Weekly summary report generation (manual or automated)  
- Simple Flask backend with HTML templates  

## Getting Started

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Run the Flask app:

flask run

3. Open your browser at http://127.0.0.1:5000 to test the prototype

---

Notes:

This is a proof of concept; the goal is to demonstrate feasibility and gather ideas for team development.
The data entered is currently stored locally; future versions may support multiple users, persistent accounts, and enhanced analytics.

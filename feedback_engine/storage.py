import sqlite3
from datetime import datetime

DB_FILE = "mindtrack.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            task TEXT NOT NULL,
            mood INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_task(user_id, task, mood):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (user_id, task, mood, date)
        VALUES (?, ?, ?, ?)
    """, (user_id, task, mood, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_tasks(user_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT task, mood, date FROM tasks
        WHERE user_id = ?
        ORDER BY date DESC
    """, (user_id,))
    data = cursor.fetchall()
    conn.close()
    return data

# Initialize DB on import
init_db()

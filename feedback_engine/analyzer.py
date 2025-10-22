from .storage import get_tasks
from datetime import datetime, timedelta

def analyze_week(user_id):
    data = get_tasks(user_id)
    if not data:
        return {"tasks": 0, "avg_mood": 0}

    one_week_ago = datetime.now() - timedelta(days=7)
    week_data = [
        (task, mood, date)
        for task, mood, date in data
        if datetime.fromisoformat(date) >= one_week_ago
    ]

    if not week_data:
        return {"tasks": 0, "avg_mood": 0}

    avg_mood = sum(int(mood) for (_, mood, _) in week_data) / len(week_data)
    return {
        "tasks": len(week_data),
        "avg_mood": round(avg_mood, 2)
    }

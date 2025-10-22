from .analyzer import analyze_week

def recommend_action(user_id):
    analysis = analyze_week(user_id)
    tasks_completed = analysis["tasks"]
    avg_mood = analysis["avg_mood"]

    if tasks_completed < 3:
        return "Try to complete at least 3 tasks this week to boost your productivity!"
    elif avg_mood < 3:
        return "Consider taking short breaks during your tasks to improve your mood."
    else:
        return "Great job! Keep up the good work and maintain your positive mood!"

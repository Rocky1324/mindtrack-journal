from .storage import save_task

def log_task(user_id, task, mood):
    if not isinstance(mood, int) or not (1 <= mood <= 5):
        raise ValueError("Mood must be an integer between 1 and 5")
    save_task(user_id, task, mood)
    return "Task logged successfully."

# Feedback Engine Module

## Description
This module handles user task logging, weekly mood analysis, and personalized recommendations.  
It is designed to integrate with the main MindTrack backend.

## Files
- **storage.py** — handles local data storage (SQLite)
- **tracker.py** — records tasks and moods
- **analyzer.py** — analyzes weekly performance
- **recommender.py** — generates personalized feedback

## Usage Example
```python
from feedback_engine.tracker import log_task
from feedback_engine.recommender import recommend_action

log_task("user1", "Finished journal entry", 4)
print(recommend_action("user1"))
```

from feedback_engine.tracker import log_task
from feedback_engine.recommender import recommend_action

log_task("user123", "Finish Hackathon module", 4)
log_task("user123", "Read a book", 5)
log_task("user123", "Go for a walk", 3)

print(recommend_action("user123"))
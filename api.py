# api.py
from flask import Flask, request, jsonify
from feedback_engine.tracker import log_task
from feedback_engine.recommender import recommend_action
from feedback_engine.storage import init_db

app = Flask(__name__)
init_db()

@app.route("/log_task", methods=["POST"])
def add_task():
    data = request.get_json()
    user_id = data.get("user_id")
    task = data.get("task")
    mood = data.get("mood")

    if not user_id or not task or mood is None:
        return jsonify({"error": "Missing user_id, task, or mood"}), 400

    try:
        log_task(user_id, task, mood)
        return jsonify({"message": "Task logged successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/recommendation/<user_id>", methods=["GET"])
def get_recommendation(user_id):
    try:
        rec = recommend_action(user_id)
        return jsonify({"user_id": user_id, "recommendation": rec})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)

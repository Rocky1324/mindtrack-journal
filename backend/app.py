from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to MindTrack Journal API"})

@app.route('/login', methods=['POST'])
def login():
    # Placeholder for login logic
    return jsonify({"status": "Login route hit"})

@app.route('/profile', methods=['POST'])
def create_profile():
    # Placeholder for profile creation
    return jsonify({"status": "Profile created"})

@app.route('/questionnaire', methods=['POST'])
def generate_plan():
    # Placeholder for questionnaire logic
    return jsonify({"plan": "Generated plan based on answers"})

if __name__ == '__main__':
    app.run(debug=True)
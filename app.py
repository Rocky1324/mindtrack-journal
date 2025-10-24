from flask import Flask, jsonify, request, render_template, os, login_required
from flask_login import LoginManager
login_manager = LoginManager()


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Placeholder for login logic
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    # Placeholder for login logic
    return jsonify({"status": "Logout route hit"})


@login_required
@app.route('/profile', methods=['POST'])
def create_profile():
    # Placeholder for profile creation
    return jsonify({"status": "Profile created"})


@app.route('/questionnaire', methods=['POST'])
@login_required
def generate_plan():
    # Placeholder for questionnaire logic
    return jsonify({"plan": "Generated plan based on answers"})

if __name__ == '__main__':
    app.run(debug=True)
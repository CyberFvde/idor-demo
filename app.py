from flask import Flask, render_template, abort

app = Flask(__name__)

# Simulated user "database"
users = {
    1: {"name": "Gavin", "email": "gavin@example.com"},
    2: {"name": "Sam", "email": "sam@example.com"}
}

# Vulnerable endpoint: It takes a user_id from the URL without checking ownership.
@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = users.get(user_id)
    if user:
        return render_template('profile.html', user=user)
    return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)

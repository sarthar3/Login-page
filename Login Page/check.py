from flask import Flask, render_template, request
import hashlib
app = Flask(__name__)
users = {
    'user1': 'password1',
    'user2': 'password2'
}
@app.route('/')
def login_page():
    return render_template('Login.html')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == users[username]:
            return f'Welcome, {username}!'
    return 'Invalid username or password'
if __name__ == '__main__':
    app.run(debug=True)

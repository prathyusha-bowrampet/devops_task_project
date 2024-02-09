from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy database for storing registered users
registered_users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in registered_users:
            return 'Username already exists!'
        registered_users[username] = password
        return 'Registration successful! You can now <a href="/login">login</a>.'
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in registered_users and registered_users[username] == password:
            session['username'] = username
            return 'Login successful!'
        else:
            return 'Invalid username or password. <a href="/register">Register</a> if you don\'t have an account.'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return 'You have been logged out.'

if __name__ == '__main__':
    app.run(debug=True)

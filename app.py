import sqlite3
import hashlib  # for hashing passwords
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to create a SQLite connection
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None

# Function to create the users table
def create_users_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT NOT NULL,
                            password TEXT NOT NULL
                        )''')
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# Function to register a user
def register(conn, username, password):
    try:
        cursor = conn.cursor()
        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, hashed_password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.Error as e:
        print(e)

# Function to log in a user (placeholder)
def login(conn, username, password):
    print("Login function")

# Route to register a user
@app.route('/register', methods=['POST'])
def register_user():
    db_file = "user.db"
    conn = create_connection(db_file)
    if conn:
        create_users_table(conn)
        username = request.form['username']
        password = request.form['password']
        phone = request.form.get('phone', '')  # Get phone number if provided
        register(conn, username, password)
        conn.close()
        return render_template('register.html', message="Registration successful!")
    else:
        return render_template('register.html', message="Registration failed. Please try again later.")

# Route to render the registration form
@app.route('/')
def index():
    return render_template('index.html')

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

# Import necessary modules
from flask import Flask, render_template, request
import sqlite3

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Connect to SQLite database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Create users table if it doesn't exist
        cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

        # Insert username and password into the table
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

        # Fetch all users from the table
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()

        # Close database connection
        conn.close()

        # Render HTML template with users data
        return render_template('index.html', users=users)
    else:
        return render_template('index.html', users=[])

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

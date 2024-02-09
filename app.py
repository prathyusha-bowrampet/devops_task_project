import sqlite3
import hashlib  # for hashing passwords

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

# Example usage
if __name__ == "__main__":
    db_file = "user.db"
    conn = create_connection(db_file)
    if conn:
        create_users_table(conn)
        register(conn, "john", "password123")
        login(conn, "john", "password123")
        conn.close()

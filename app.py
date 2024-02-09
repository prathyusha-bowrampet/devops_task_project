import sqlite3

# Function to create a SQLite connection and cursor
def create_connection():
    try:
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        return conn, cursor
    except sqlite3.Error as e:
        print(e)
    return None, None

# Function to create a users table in SQLite database if not exists
def create_users_table():
    conn, cursor = create_connection()
    if conn:
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                username TEXT NOT NULL,
                                password TEXT NOT NULL
                            )''')
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

# Function to register a user and store details in the SQLite database
def register(username, password):
    create_users_table()  # Ensure users table exists
    conn, cursor = create_connection()
    if conn:
        try:
            cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
            conn.commit()
            print("User registered successfully!")
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

# Function to log in a user (just a placeholder)
def login(username, password):
    print("Login function")

# Example usage
if __name__ == "__main__":
    # Register a user
    register("john", "password123")
    # Log in a user
    login("john", "password123")

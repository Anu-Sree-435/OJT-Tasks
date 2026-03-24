import sqlite3

def connect():
    conn = sqlite3.connect("eventease.db")
    return conn

def setup_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        venue TEXT,
        time TEXT,
        capacity INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registrations(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        event_id INTEGER,
        checked_in INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rating INTEGER,
        comments TEXT
    )
    """)

    # Default users
    cursor.execute("INSERT INTO users(username, password, role) VALUES ('admin','1234','admin')")
    cursor.execute("INSERT INTO users(username, password, role) VALUES ('volunteer','1234','volunteer')")

    conn.commit()
    conn.close()

from db import connect

def add_event(title, venue, time, capacity):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO events(title, venue, time, capacity) VALUES (?, ?, ?, ?)",
                   (title, venue, time, capacity))

    conn.commit()
    conn.close()

def get_events():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM events")
    data = cursor.fetchall()

    conn.close()
    return data

def add_participant(name, email, event_id, qr):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO participants(name, email, event_id, qr_code) VALUES (?, ?, ?, ?)",
                   (name, email, event_id, qr))

    conn.commit()
    conn.close()

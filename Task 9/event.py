import tkinter as tk
from db import connect

def create_event_ui(root):

    def save():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO events(title, venue, time, capacity) VALUES (?,?,?,?)",
                       (title.get(), venue.get(), time.get(), capacity.get()))

        conn.commit()
        conn.close()

    win = tk.Toplevel(root)
    win.title("Create Event")

    title = tk.Entry(win)
    venue = tk.Entry(win)
    time = tk.Entry(win)
    capacity = tk.Entry(win)

    tk.Label(win, text="Title").pack()
    title.pack()

    tk.Label(win, text="Venue").pack()
    venue.pack()

    tk.Label(win, text="Time").pack()
    time.pack()

    tk.Label(win, text="Capacity").pack()
    capacity.pack()

    tk.Button(win, text="Create", command=save).pack()

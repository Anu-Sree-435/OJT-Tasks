import tkinter as tk
from db import connect

def create_event_ui(root):

    def save():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO events(title, venue, time, capacity) VALUES (?,?,?,?)",
            (title.get(), venue.get(), time.get(), capacity.get())
        )

        conn.commit()
        conn.close()

        status.config(text="Event Created Successfully ✅", fg="green")

        title.delete(0, tk.END)
        venue.delete(0, tk.END)
        time.delete(0, tk.END)
        capacity.delete(0, tk.END)

    win = tk.Toplevel(root)
    win.title("Create Event")
    win.geometry("350x250")

    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=2)

    tk.Label(win, text="Title").grid(row=0, column=0, padx=10, pady=8, sticky="e")
    title = tk.Entry(win)
    title.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(win, text="Venue").grid(row=1, column=0, padx=10, pady=8, sticky="e")
    venue = tk.Entry(win)
    venue.grid(row=1, column=1, padx=10, pady=8)

    tk.Label(win, text="Time").grid(row=2, column=0, padx=10, pady=8, sticky="e")
    time = tk.Entry(win)
    time.grid(row=2, column=1, padx=10, pady=8)

    tk.Label(win, text="Capacity").grid(row=3, column=0, padx=10, pady=8, sticky="e")
    capacity = tk.Entry(win)
    capacity.grid(row=3, column=1, padx=10, pady=8)

    tk.Button(win, text="Create Event", command=save)\
        .grid(row=4, column=0, columnspan=2, pady=15)

    status = tk.Label(win, text="")
    status.grid(row=5, column=0, columnspan=2)
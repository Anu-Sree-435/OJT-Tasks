import tkinter as tk
from db import connect

def register_ui(root):

    def register():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO registrations(name, event_id) VALUES (?,?)",
                       (name.get(), event_id.get()))

        conn.commit()
        conn.close()

    win = tk.Toplevel(root)
    win.title("Register")

    name = tk.Entry(win)
    event_id = tk.Entry(win)

    tk.Label(win, text="Name").pack()
    name.pack()

    tk.Label(win, text="Event ID").pack()
    event_id.pack()

    tk.Button(win, text="Register", command=register).pack()

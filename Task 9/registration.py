import tkinter as tk
from db import connect

def register_ui(root):

    def register():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO registrations(name, event_id) VALUES (?,?)",
            (name.get(), event_id.get())
        )

        conn.commit()
        conn.close()

        status.config(text="Registered Successfully ✅", fg="green")

        name.delete(0, tk.END)
        event_id.delete(0, tk.END)

    win = tk.Toplevel(root)
    win.title("Event Registration")
    win.geometry("350x220")

    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=2)

    tk.Label(win, text="Name").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    name = tk.Entry(win)
    name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(win, text="Event ID").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    event_id = tk.Entry(win)
    event_id.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(win, text="Register", command=register)\
        .grid(row=2, column=0, columnspan=2, pady=15)

    status = tk.Label(win, text="")
    status.grid(row=3, column=0, columnspan=2)
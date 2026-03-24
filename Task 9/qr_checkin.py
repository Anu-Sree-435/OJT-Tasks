import tkinter as tk
from db import connect

def checkin_ui(root):

    def checkin():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE registrations SET checked_in=1 WHERE id=?",
            (reg_id.get(),)
        )

        conn.commit()
        conn.close()

        status.config(text="Check-in Successful ✅", fg="green")

        reg_id.delete(0, tk.END)

    win = tk.Toplevel(root)
    win.title("QR Check-in")
    win.geometry("350x200")

    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=2)

    tk.Label(win, text="Registration ID").grid(row=0, column=0, padx=10, pady=15, sticky="e")
    reg_id = tk.Entry(win)
    reg_id.grid(row=0, column=1, padx=10, pady=15)

    tk.Button(win, text="Check-in", command=checkin)\
        .grid(row=1, column=0, columnspan=2, pady=15)

    status = tk.Label(win, text="")
    status.grid(row=2, column=0, columnspan=2)
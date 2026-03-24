import tkinter as tk
from db import connect

def checkin_ui(root):

    def checkin():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("UPDATE registrations SET checked_in=1 WHERE id=?",
                       (reg_id.get(),))

        conn.commit()
        conn.close()

    win = tk.Toplevel(root)
    win.title("QR Check-in")

    reg_id = tk.Entry(win)

    tk.Label(win, text="Registration ID").pack()
    reg_id.pack()

    tk.Button(win, text="Check-in", command=checkin).pack()

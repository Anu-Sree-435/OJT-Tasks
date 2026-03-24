import tkinter as tk
from db import connect

def dashboard_ui(root):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM registrations")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM registrations WHERE checked_in=1")
    checked = cursor.fetchone()[0]

    win = tk.Toplevel(root)
    win.title("Dashboard")

    tk.Label(win, text=f"Total Registrations: {total}").pack()
    tk.Label(win, text=f"Checked-in: {checked}").pack()

    conn.close()

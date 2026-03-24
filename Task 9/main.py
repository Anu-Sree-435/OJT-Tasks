import tkinter as tk
from db import setup_db
from login import login_ui
from event import create_event_ui
from registration import register_ui
from qr_checkin import checkin_ui
from dashboard import dashboard_ui
from feedback import feedback_ui

setup_db()

root = tk.Tk()
root.title("EventEase")

tk.Button(root, text="Login", command=lambda: login_ui(root)).pack()
tk.Button(root, text="Create Event", command=lambda: create_event_ui(root)).pack()
tk.Button(root, text="Register", command=lambda: register_ui(root)).pack()
tk.Button(root, text="Check-in", command=lambda: checkin_ui(root)).pack()
tk.Button(root, text="Dashboard", command=lambda: dashboard_ui(root)).pack()
tk.Button(root, text="Feedback", command=lambda: feedback_ui(root)).pack()

root.mainloop()

import tkinter as tk
from db import connect

def login_ui(root):

    def login():
        user = username.get()
        pwd = password.get()

        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (user, pwd))
        result = cursor.fetchone()

        if result:
            tk.Label(win, text="Login Success").pack()
        else:
            tk.Label(win, text="Invalid Login").pack()
            root.iconify()

    win = tk.Toplevel(root)
    win.title("Login")

    tk.Label(win, text="Username").pack()
    username = tk.Entry(win)
    username.pack()

    tk.Label(win, text="Password").pack()
    password = tk.Entry(win, show="*")
    password.pack()

    tk.Button(win, text="Login", command=login).pack()
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
            status.config(text="Login Success", fg="green")
        else:
            status.config(text="Invalid Login", fg="red")

    win = tk.Toplevel(root)
    win.title("Login")

    win.geometry("300x200")

    tk.Label(win, text="Username").grid(row=0, column=0, padx=10, pady=10)
    username = tk.Entry(win)
    username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(win, text="Password").grid(row=1, column=0, padx=10, pady=10)
    password = tk.Entry(win, show="*")
    password.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(win, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)

    status = tk.Label(win, text="")
    status.grid(row=3, column=0, columnspan=2)
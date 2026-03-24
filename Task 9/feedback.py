import tkinter as tk
from db import connect

def feedback_ui(root):

    def submit():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO feedback(name, rating, comments) VALUES (?,?,?)",
                       (name.get(), rating.get(), comments.get()))

        conn.commit()
        conn.close()

    win = tk.Toplevel(root)
    win.title("Feedback")

    name = tk.Entry(win)
    rating = tk.Entry(win)
    comments = tk.Entry(win)

    tk.Label(win, text="Name").pack()
    name.pack()

    tk.Label(win, text="Rating").pack()
    rating.pack()

    tk.Label(win, text="Comments").pack()
    comments.pack()

    tk.Button(win, text="Submit", command=submit).pack()

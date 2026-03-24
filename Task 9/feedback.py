import tkinter as tk
from db import connect

def feedback_ui(root):

    def submit():
        conn = connect()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO feedback(name, rating, comments) VALUES (?,?,?)",
            (name.get(), rating.get(), comments.get())
        )

        conn.commit()
        conn.close()

        status.config(text="Feedback Submitted ✅", fg="green")

        name.delete(0, tk.END)
        rating.delete(0, tk.END)
        comments.delete(0, tk.END)

    win = tk.Toplevel(root)
    win.title("Feedback")
    win.geometry("350x250")

    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=2)

    tk.Label(win, text="Name").grid(row=0, column=0, padx=10, pady=8, sticky="e")
    name = tk.Entry(win)
    name.grid(row=0, column=1, padx=10, pady=8)

    tk.Label(win, text="Rating (1-5)").grid(row=1, column=0, padx=10, pady=8, sticky="e")
    rating = tk.Entry(win)
    rating.grid(row=1, column=1, padx=10, pady=8)

    tk.Label(win, text="Comments").grid(row=2, column=0, padx=10, pady=8, sticky="e")
    comments = tk.Entry(win)
    comments.grid(row=2, column=1, padx=10, pady=8)

    tk.Button(win, text="Submit", command=submit)\
        .grid(row=3, column=0, columnspan=2, pady=15)

    status = tk.Label(win, text="")
    status.grid(row=4, column=0, columnspan=2)
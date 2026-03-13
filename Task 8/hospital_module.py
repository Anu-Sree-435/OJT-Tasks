import tkinter as tk
import sqlite3

def update_stock():
    conn = sqlite3.connect("blood_bank.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO blood_stock(blood_group,units) VALUES(?,?)",
                   (blood.get(), units.get()))

    conn.commit()
    conn.close()

    print("Stock Updated")

root = tk.Tk()
root.title("Blood Stock")

blood = tk.StringVar()
units = tk.StringVar()

tk.Label(root,text="Blood Group").pack()
tk.Entry(root,textvariable=blood).pack()

tk.Label(root,text="Units").pack()
tk.Entry(root,textvariable=units).pack()

tk.Button(root,text="Update Stock",command=update_stock).pack()

root.mainloop()

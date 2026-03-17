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
    root.destroy()

root = tk.Tk()
root.title("Blood Stock")

blood = tk.StringVar()
units = tk.StringVar()

tk.Label(root,text="Blood Group").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=blood).grid(row=0, column=1)

tk.Label(root,text="Units").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=units).grid(row=1, column=1)

tk.Button(root,text="Update Stock",command=update_stock).grid(row=3, column=1, padx=10)

root.mainloop()

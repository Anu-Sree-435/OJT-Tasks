import tkinter as tk
import sqlite3

def add_donor():
    conn = sqlite3.connect("blood_bank.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO donors(name,phone,address,blood_group,age,health,last_donation) VALUES(?,?,?,?,?,?,?)",
(name.get(), phone.get(), address.get(), blood.get(), age.get(), health.get(), last.get())
)

    conn.commit()
    conn.close()

    print("Donor Added")
    root.destroy()

root = tk.Tk()
root.title("Donor Registration")

name = tk.StringVar()
phone = tk.StringVar()
address = tk.StringVar()
blood = tk.StringVar()
age = tk.StringVar()
health = tk.StringVar()
last = tk.StringVar()

tk.Label(root,text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=name).grid(row=0, column=1)

tk.Label(root,text="Phone").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=phone).grid(row=1, column=1)

tk.Label(root,text="Address").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=address).grid(row=2, column=1)

tk.Label(root,text="Blood Group").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=blood).grid(row=3, column=1)

tk.Label(root,text="Age").grid(row=4, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=age).grid(row=4, column=1)

tk.Label(root,text="Health Details").grid(row=5, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=health).grid(row=5, column=1)

tk.Label(root,text="Last Donation Date").grid(row=6, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=last).grid(row=6, column=1)

tk.Button(root,text="Register",command=add_donor).grid(row=7, column=1, padx=10)
root.mainloop()

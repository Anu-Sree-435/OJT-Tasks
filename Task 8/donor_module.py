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

root = tk.Tk()
root.title("Donor Registration")

name = tk.StringVar()
phone = tk.StringVar()
address = tk.StringVar()
blood = tk.StringVar()
age = tk.StringVar()
health = tk.StringVar()
last = tk.StringVar()

tk.Label(root,text="Name").pack()
tk.Entry(root,textvariable=name).pack()

tk.Label(root,text="Phone").pack()
tk.Entry(root,textvariable=phone).pack()

tk.Label(root,text="Address").pack()
tk.Entry(root,textvariable=address).pack()

tk.Label(root,text="Blood Group").pack()
tk.Entry(root,textvariable=blood).pack()

tk.Label(root,text="Age").pack()
tk.Entry(root,textvariable=age).pack()

tk.Label(root,text="Health Details").pack()
tk.Entry(root,textvariable=health).pack()

tk.Label(root,text="Last Donation Date").pack()
tk.Entry(root,textvariable=last).pack()

tk.Button(root,text="Register",command=add_donor).pack()

root.mainloop()

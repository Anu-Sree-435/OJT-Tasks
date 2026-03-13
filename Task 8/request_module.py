import tkinter as tk
import sqlite3

def create_request():
    conn = sqlite3.connect("blood_bank.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO requests(patient_name,blood_group,location,urgency) VALUES(?,?,?,?)",
                   (patient.get(), blood.get(), location.get(), urgency.get()))

    conn.commit()
    conn.close()

    print("Request Created")

root = tk.Tk()
root.title("Blood Request")

patient = tk.StringVar()
blood = tk.StringVar()
location = tk.StringVar()
urgency = tk.StringVar()

tk.Label(root,text="Patient Name").pack()
tk.Entry(root,textvariable=patient).pack()

tk.Label(root,text="Blood Group").pack()
tk.Entry(root,textvariable=blood).pack()

tk.Label(root,text="Location").pack()
tk.Entry(root,textvariable=location).pack()

tk.Label(root,text="Urgency").pack()
tk.Entry(root,textvariable=urgency).pack()

tk.Button(root,text="Submit Request",command=create_request).pack()

root.mainloop()

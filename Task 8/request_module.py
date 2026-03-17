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
    root.destroy()

root = tk.Tk()
root.title("Blood Request")

patient = tk.StringVar()
blood = tk.StringVar()
location = tk.StringVar()
urgency = tk.StringVar()

tk.Label(root,text="Patient Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=patient).grid(row=0, column=1)

tk.Label(root,text="Blood Group").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=blood).grid(row=1, column=1)

tk.Label(root,text="Location").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=location).grid(row=2, column=1)

tk.Label(root,text="Urgency").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(root,textvariable=urgency).grid(row=3, column=1)

tk.Button(root,text="Submit Request",command=create_request).grid(row=4, column=1, padx=10)

root.mainloop()

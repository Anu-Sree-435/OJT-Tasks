import tkinter as tk
import os

def donor():
    root.iconify()
    os.system("python donor_module.py")

def request():
    root.iconify()
    os.system("python request_module.py")

def hospital():
    root.iconify()
    os.system("python hospital_module.py")

root = tk.Tk()
root.title("Blood Donation Management System")

tk.Button(root,text="Donor Module",command=donor).pack(pady=10)
tk.Button(root,text="Blood Request",command=request).pack(pady=10)
tk.Button(root,text="Hospital Module",command=hospital).pack(pady=10)

root.mainloop()

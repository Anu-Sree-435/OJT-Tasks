import tkinter as tk
import pandas as pd

def submit():
    data = {
        "Name": name.get(),
        "Age": age.get(),
        "Gender": gender.get(),
        "City": city.get(),
        "Department": dept.get(),
        "Salary": salary.get()
    }
    df = pd.DataFrame([data])
    df.to_csv("user_data.csv", mode='a', index=False, header=False)
    clear()

def clear():
    name.set(""); age.set(""); gender.set(""); city.set(""); dept.set(""); salary.set("")

root = tk.Tk()
root.title("User Data Form")

name = tk.StringVar()
age = tk.StringVar()
gender = tk.StringVar()
city = tk.StringVar()
dept = tk.StringVar()
salary = tk.StringVar()

fields = ["Name","Age","Gender","City","Department","Salary"]
vars = [name,age,gender,city,dept,salary]

for i, field in enumerate(fields):
    tk.Label(root, text=field).grid(row=i, column=0)
    tk.Entry(root, textvariable=vars[i]).grid(row=i, column=1)

tk.Button(root, text="Submit", command=submit).grid(row=6, column=0)
tk.Button(root, text="Reset", command=clear).grid(row=6, column=1)

root.mainloop()

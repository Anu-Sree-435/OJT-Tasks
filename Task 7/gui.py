import tkinter as tk

def start_gui(callback):

    root = tk.Tk()
    root.title("SmartRetail - Sales Entry")
    root.geometry("300x250")

    tk.Label(root, text="Product Name").pack()
    entry_product = tk.Entry(root)
    entry_product.pack()

    tk.Label(root, text="Category").pack()
    entry_category = tk.Entry(root)
    entry_category.pack()

    tk.Label(root, text="Unit Price").pack()
    entry_price = tk.Entry(root)
    entry_price.pack()

    tk.Label(root, text="Quantity").pack()
    entry_quantity = tk.Entry(root)
    entry_quantity.pack()

    def submit():
        product = entry_product.get()
        category = entry_category.get()
        price = entry_price.get()
        quantity = entry_quantity.get()

        callback(product, category, price, quantity)

        entry_product.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)

    tk.Button(root, text="Submit", command=submit).pack(pady=10)

    root.mainloop()
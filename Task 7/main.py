from logic import process_sales
import gui
import database
import report

def handle_data(product, category, price, quantity):
    price = float(price)
    quantity = int(quantity)
    total, tax, profit = process_sales(price, quantity)
    product_id = database.add_product(product, category, price)
    database.record_sale(product_id, quantity, total)
    report.generate_report()

database.create_tables()
gui.start_gui(handle_data)
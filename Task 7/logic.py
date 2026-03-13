def process_sales(price, quantity):

    total_sales = price * quantity
    tax = total_sales * 0.05
    profit = total_sales * 0.20

    return total_sales, tax, profit
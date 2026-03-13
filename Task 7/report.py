import pandas as pd
import sqlite3

def generate_report():

    conn = sqlite3.connect("smartretail.db")

    query = """
    SELECT p.ProductName,
           p.Category,
           p.UnitPrice,
           s.Quantity,
           s.TotalSales,
           s.Timestamp
    FROM sales s
    JOIN products p
    ON p.ProductID = s.ProductID
"""

    df = pd.read_sql_query(query, conn)

    df.to_excel("sales_report.xlsx", index=False)

    conn.close()

    print("Excel Report Generated ✅")
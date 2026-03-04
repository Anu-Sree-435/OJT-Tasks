import sqlite3

DB_NAME = "smartretail.db"


def create_tables():

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Products Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products(
            ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProductName TEXT,
            Category TEXT,
            UnitPrice REAL,
            StockLevel INTEGER
        )
    """)

    # Sales Table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales(
            TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProductID INTEGER,
            Quantity INTEGER,
            TotalSales REAL,
            Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def add_product(name, category, price):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO products(ProductName, Category, UnitPrice, StockLevel)
        VALUES (?, ?, ?, 100)
    """, (name, category, price))

    conn.commit()
    pid = cur.lastrowid
    conn.close()

    return pid


def record_sale(product_id, quantity, total):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO sales(ProductID, Quantity, TotalSales)
        VALUES (?, ?, ?)
    """, (product_id, quantity, total))

    conn.commit()
    conn.close()
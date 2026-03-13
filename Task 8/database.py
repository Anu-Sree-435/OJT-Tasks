import sqlite3

conn = sqlite3.connect("blood_bank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS donors(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
phone TEXT,
address TEXT,
blood_group TEXT,
age INTEGER,
health TEXT,
last_donation TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS requests(
id INTEGER PRIMARY KEY AUTOINCREMENT,
patient_name TEXT,
blood_group TEXT,
location TEXT,
urgency TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS blood_stock(
blood_group TEXT,
units INTEGER
)
""")

import sqlite3

conn = sqlite3.connect("blood_bank.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM donors")
donors = cursor.fetchone()

cursor.execute("SELECT COUNT(*) FROM requests")
requests = cursor.fetchone()

print("Total Donors:", donors[0])
print("Total Requests:", requests[0])

conn.close()

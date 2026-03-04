import sqlite3
import pandas as pd

conn = sqlite3.connect("user_data.db")
df = pd.read_csv("cleaned_data.csv")

df.to_sql("employees", conn, if_exists="replace", index=False)
conn.close()



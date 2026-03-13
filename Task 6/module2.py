import pandas as pd

df = pd.read_csv("user_data.csv")

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df["Age"] = pd.to_numeric(df["Age"], errors='coerce')
df["Salary"] = pd.to_numeric(df["Salary"], errors='coerce')

df.to_csv("cleaned_data.csv", index=False)

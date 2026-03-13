import pandas as pd

df = pd.read_csv("cleaned_data.csv")   

df.to_excel("final.xlsx", index=False)





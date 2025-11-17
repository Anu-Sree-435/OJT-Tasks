import requests
from bs4 import BeautifulSoup
import pandas as pd

product = input("Enter product name: ")

url = f"https://www.flipkart.com/search?q={product}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/123.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titles = []
prices = []
links = []
sellers = []

for item in soup.find_all("div", {"class": "cPHDOP col-12-12"}):
    title_tag = item.find("div", {"class": "KzDlHZ"})
    price_tag = item.find("div", {"class": "Nx9bqj"})
    link_tag = item.find("a", href=True)
    seller_tag = item.find("div", {"class": "KTpSwS"})
    
    if title_tag and price_tag and link_tag:
        titles.append(title_tag.text.strip())
        prices.append(price_tag.text.strip())
        links.append("https://www.flipkart.com" + link_tag["href"])
        sellers.append(seller_tag.text.strip() if seller_tag else "Not Available")
     
data = pd.DataFrame({
     "Seller": sellers,
    "Product Name": titles,
    "Price": prices,
    "URL": links

    })

data.drop_duplicates(inplace=True)
data.dropna(inplace=True)

if not data.empty:
    data.to_csv("flipkart_products.csv", index=False, encoding="utf-8")
    print("✅ Data saved successfully as 'flipkart_products.csv'")
else:
    print("⚠️ No data found — try keywords like: mobile, laptop, shoes, TV, etc.")
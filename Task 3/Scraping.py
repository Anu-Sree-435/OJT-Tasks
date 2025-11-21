from bs4 import BeautifulSoup
import requests
import pandas as pd

def scrape_indiamart(product):
    url = f"https://dir.indiamart.com/search.mp?ss={product.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

   
    product_cards = soup.select(
        "div.card"
    )

    data = []

    for card in product_cards:

        product_name_tag = (
            card.select_one("fs_18") or
            card.select_one("h2") or
            card.select_one(".product-title") or
            card.select_one("a")
        )
        product_name = product_name_tag.get_text(strip=True) if product_name_tag else "N/A"

        price_tag = (
            card.select_one(".price") or
            card.select_one(".prd_price") or
            card.select_one(".f_price") or
            card.select_one(".nm_price")
        )
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        seller_tag = (
            card.select_one(".c_name") or
            card.select_one(".cmpny") or
            card.select_one(".seller-name") or
            card.select_one(".store-name")
        )
        seller = seller_tag.get_text(strip=True) if seller_tag else "N/A"

        link_tag = card.select_one("a") or card.find("a", href=True)
        url = "https://dir.indiamart.com" + link_tag.get("href") if link_tag else "N/A"

        data.append({
            "Seller": seller,
            "Product": product_name,
            "Price": price,
            "URL": url
        })

    return pd.DataFrame(data)

product = input("Enter product: ")
df = scrape_indiamart(product)
print(df)
filename = f"{product.replace(' ', '_')}.csv"
df.to_csv(filename, index=False)
print("\nSaved to:", filename)
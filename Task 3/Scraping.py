from bs4 import BeautifulSoup
import requests
import pandas as pd

product = input("Enter product:  ")
data = []

def scrape_indiamart(product):
    url = f"https://dir.indiamart.com/search.mp?ss={product.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    product_cards = soup.select( "div.card" )
    
    for card in product_cards:

        product_name_tag = (
            card.
            select_one(".fs_18") or
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
            card.select_one(".company-location") or
            card.select_one(".companyname") or
            card.select_one("h4.company-location") or
            card.select_one(".store-name")
        )
        seller = seller_tag.get_text(strip=True) if seller_tag else "N/A"

        link_tag = card.select_one("a") or card.find("a", href=True)
        url = "https://dir.indiamart.com" + link_tag.get("href") if link_tag else "N/A"

        data.append({
            "Platform": "IndiaMart",
            "Product": product_name,
            "Seller": "seller",
            "Price": price,
            "URL": url
            
        })
        

def scrape_flipkart(product):
    url = f"https://www.flipkart.com/search?q={product.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
   
    product_cards = soup.find_all("div", {"class": "_75nlfW"})

    for card in product_cards:
        name_tag = card.find("div", {"class": "KzDlHZ"}) or \
         card.find("a", {"class": "wjcEIp"})
        product_name = name_tag.get_text(strip=True) if name_tag else "N/A"

        price_tag = card.find("div", {"class": "Nx9bqj"})
        price = price_tag.get_text(strip=True) if price_tag else "N/A"
        
        link_tag = card.find("a", href=True)
        link = "https://www.flipkart.com" + link_tag["href"] if link_tag else "N/A"

        data.append({
            "Platform": "Flipkart",
            "Product": product_name,
            "Seller": "N/A",
            "Price": price,
            "URL": link
        })
      
scrape_indiamart(product)
scrape_flipkart(product)

df= pd.DataFrame(data)
df.to_csv(f"{product.replace(' ', '_')}.csv", index=False)
print("\nSaved as csv")

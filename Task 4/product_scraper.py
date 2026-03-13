from bs4 import BeautifulSoup
import requests


def scrape_flipkart(product):
    url = f"https://www.flipkart.com/search?q={product.replace(' ', '+')}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")

    data = []

    product_cards = soup.find_all("div", {"class": "lvJbLV"}) or soup.find_all("div", {"class": "LwDgZ8"}) or soup.find_all("div", {"class": "nZIRY7"}) 

    for card in product_cards:
        name_tag = card.find("a", {"class": "pIpigb"}) or \
         card.find("div", {"class": "RG5Slk"})
        if not name_tag:
            continue
        product_name = name_tag.get_text(strip=True) if name_tag else "N/A"
            
        price_tag = card.find("div", {"class": "hZ3P6w"})
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        rating_tag = card.find("div", {"class": "MKiFS6"})
        review_span = card.select_one("span.PvbNMB span:nth-child(3)")

        reviews = 0

        review_span = card.select_one("span.PvbNMB span:nth-child(3)") or card.find("span", {"class": "PvbNMB"})
        if review_span:
            reviews = int(
                review_span.text
                .replace("Reviews", "")
                .replace(",", "")
                .replace("(", "")
                .replace(")", "")
                .strip())


     
        data.append({
            "Product_Name": product_name,
            "Price": int(price_tag.text.replace("₹", "").replace(",", "")) if price_tag else 0,
            "Rating": float(rating_tag.text) if rating_tag else 0,
            "Review_Count": reviews,
            "url": "https://www.flipkart.com" + card.find("a")["href"]
        })

    return data

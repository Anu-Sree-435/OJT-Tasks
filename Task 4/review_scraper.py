import requests
import json
import os
import time
from bs4 import BeautifulSoup

def scrape_reviews(product_url):
    reviews = []
    page = 1
    product_id = product_url.split("/")[-1].split("?")[0]


    while page <= 5:  
        url = f"{product_url}&page={page}"
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")

        blocks = soup.select("div.G4PxIA")
        if not blocks:
            break

        for b in blocks:
            reviews.append(b.text.strip())

        page += 1
        time.sleep(1)
        os.makedirs("reviews", exist_ok=True)

    with open(f"reviews/{product_id}.json", "w", encoding="utf-8") as f:
        json.dump(reviews, f, indent=2, ensure_ascii=False)


    return reviews

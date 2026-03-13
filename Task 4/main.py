import os
import json
from product_scraper import scrape_flipkart
from filter_products import filter_by_reviews
from scoring import filter_by_score
from review_scraper import scrape_reviews
from trending import get_trending_products
from top_selling import get_top_selling_products

os.makedirs("output", exist_ok=True)

product = input("Enter product: ")

products = scrape_flipkart(product)
filtered = filter_by_reviews(products)
scored = filter_by_score(filtered)

for p in scored:
    p["reviews_text"] = scrape_reviews(p["url"])

final_output = {
    "scored_products": scored,
    "trending": get_trending_products(scored),
    "top_selling": get_top_selling_products(scored)
}

with open("output/final_output.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=4)

print("Final output saved")

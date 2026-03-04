from product_scraper import scrape_flipkart
from filter_products import filter_by_reviews
from scoring import filter_by_score

def scrape_by_category_and_budget(category, min_price, max_price):
    data = scrape_flipkart(category)

    budget_filtered = [
        p for p in data if min_price <= p["Price"] <= max_price
    ]

    review_filtered = filter_by_reviews(budget_filtered)
    final_products = filter_by_score(review_filtered)

    return final_products



def calculate_score(product):
    rating_weight = 3
    review_weight = 2
    price_weight = 2
    discount_weight = 3

    score = (
        product.get("Rating", 0) * rating_weight +
        (product.get("Review_Count", 0) / 5000) * review_weight -
        (product.get("Price", 0) / 20000) * price_weight +
        (product.get("Discount", 0) / 100) * discount_weight
    )
    return round(min(score, 10), 2)


def filter_by_score(products, min_score=5):
    for p in products:
        p["score"] = calculate_score(p)
    return [p for p in products if p["score"] > min_score]

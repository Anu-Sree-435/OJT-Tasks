def filter_by_reviews(data, min_reviews=20):
    return [p for p in data if p["Review_Count"] > min_reviews]

import json
import os
from datetime import datetime

def get_trending_products(products):
    trending = sorted(
        products,
        key=lambda x: (x["Review_Count"], x["Rating"]),
        reverse=True
    )[:10]

    output = {
        "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "trending_products": trending
    }

    os.makedirs("trending", exist_ok=True)

    with open("trending/trending_products.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return trending
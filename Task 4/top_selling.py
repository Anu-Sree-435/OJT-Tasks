import json
import os
from datetime import datetime

def get_top_selling_products(products):
    top_selling = sorted(
        products,
        key=lambda x: x["Review_Count"],
        reverse=True
    )[:10]

    output = {
        "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "top_selling_products": top_selling
    }

    os.makedirs("top_selling", exist_ok=True)

    with open("top_selling/top_selling_products.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    return top_selling
"""
exit_intent_discount_engine.py - Calculates safe promotional discount that maintains minimum required gross margin
"""
import sys
import json


def calculate_margin_discount(margin_data_json: str):
    import json
    data = json.loads(margin_data_json) if isinstance(margin_data_json, str) else margin_data_json
    price = data.get("retail_price_usd", 100.0)
    cost = data.get("cost_usd", 50.0)
    min_margin = data.get("min_margin_pct", 20.0)
    max_discount_usd = price - cost - (price * (min_margin / 100.0))
    discount_pct = min(max(round((max_discount_usd / price) * 100, 1), 0.0), 20.0)
    return {"authorized_discount_pct": discount_pct, "status": "COUPON_GENERATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "exit-intent-discount-engine"}))

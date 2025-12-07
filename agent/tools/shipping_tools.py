import json

def check_shipping_price(origin: str, dest: str, weight_kg: float) -> str:
    """Calculates shipping cost."""
    if not origin or not dest:
        return json.dumps({
            "code": 400, 
            "msg": "Missing Info: Please provide both Origin and Destination cities."
        })
    if not weight_kg or weight_kg <= 0:
         return json.dumps({
            "code": 400, 
            "msg": "Invalid Weight: Weight must be greater than 0."
        })

    cost = weight_kg * 5.50 + 10
    return json.dumps({"price": f"${cost:.2f}", "currency": "USD", "service": "Standard Ground"})

def create_shipment(origin: str, dest: str) -> str:
    """Generates a new shipping label."""
    if not origin or not dest:
        return json.dumps({
            "code": 400, 
            "msg": "Missing Info: Cannot create shipment without Origin and Destination."
        })

    return json.dumps({"tracking_number": "NEW-SHIP-777", "label_url": "http://labels.com/777.pdf"})
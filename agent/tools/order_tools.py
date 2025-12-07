import json
from typing import List

def print_labels(customer_numbers: List[str], print_type: str = "A4", print_invoice: str = "invoice") -> str:
    """Generates a PDF label for specific orders."""
    
    # If the list is empty or None, return a JSON error
    if not customer_numbers or customer_numbers == [""]:
        return json.dumps({
            "code": 400, 
            "msg": "Missing Input: No customer numbers provided. Please ask the user for the Order ID."
        })

    print(f"\n[API LOG]  Requesting Labels for: {customer_numbers}")
    
    # mock response
    return json.dumps({
        "code": 0,
        "msg": "调用成功",
        "data": {"url": "http://www.cntodd.top//label.pdf"}
    })

def delete_order(customer_number: str) -> str:
    """Deletes a specific shipping order."""
    
    #  Missing Input ---
    if not customer_number:
         return json.dumps({
            "code": 400, 
            "msg": "Missing Input: No customer number provided. Please ask the user for the Order ID."
        })

    print(f"\n[API LOG]  Attempting to Delete Order: {customer_number}")
    
    return json.dumps({
        "code": -1,
        "msg": "删除失败：运单已收货，不可删除" 
    })
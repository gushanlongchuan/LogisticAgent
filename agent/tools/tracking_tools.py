import json
from typing import List

# 1. Pickup Info
def check_pickup_info(waybill_numbers: List[str]) -> str:
    """Checks pickup status/driver for waybill numbers."""
    if not waybill_numbers or waybill_numbers == [""]:
        return json.dumps({"code": 400, "msg": "Please provide a Waybill Number to check pickup status."})

    # ... (Rest of existing logic) ...
    return json.dumps({
        "msg": "success", "code": 0,
        "data": [{
            "searchNumber": "5722916732", "pickupstatusname": "待确认",
            "drivername": "小聂同学呀", "pickuptime": "2022-11-22 09:48:43"
        }]
    })

# 2. Channel Info
def get_channel_info() -> str:
    """Lists available shipping channels."""
    print(f"\n[API LOG]   Fetching Channel List...")
    return json.dumps({
        "code": 0, "msg": "调用成功",
        "data": [
            {"channelname": "中国邮政", "channelnameen": "China Post"},
            {"channelname": "香港TNT", "channelnameen": "Hong Kong TNT"},
            {"channelname": "美森快船", "channelnameen": "Mason Clippers"}
        ]
    })

# 3. Waybill Info
def get_waybill_info(customer_numbers: List[str]) -> str:
    """Retrieves tracking details using Customer Numbers."""
    if not customer_numbers or customer_numbers == [""]:
        return json.dumps({"code": 400, "msg": "Please provide a Customer Number (e.g., T620...) to find the waybill."})

    return json.dumps({
        "code": 0, "msg": "调用成功",
        "data": {
            "customernumber": [
                {
                    "customernumber": "T620200611-1001",
                    "waybillnumber": "926129030293605",
                    "tracknumber": "1Z76V3R40448621361"
                }
            ]
        }
    })

# 4. Currency Info
def get_supported_currencies() -> str:
    """Lists supported currencies."""
    print(f"\n[API LOG] Fetching Currencies...")
    return json.dumps({
        "code": 0, "msg": "调用成功",
        "data": [
            {"code": "CNY", "enname": "CNY"},
            {"code": "HKG", "enname": "HKG"},
            {"code": "USD", "enname": "USD"}
        ]
    })
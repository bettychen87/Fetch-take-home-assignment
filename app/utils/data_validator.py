def validate_receipt_data(receipt_data):
    required_fields = ["retailer", "purchaseDate", "purchaseTime", "items"]

    for field in required_fields:
        if field not in receipt_data:
            return False

    if "items" in receipt_data:
        for item in receipt_data["items"]:
            if "shortDescription" not in item or "price" not in item:
                return False
    return True

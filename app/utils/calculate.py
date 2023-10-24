from datetime import datetime, time
import math

def calculate_points(receipt_data):
    points = 0
    for char in receipt_data["retailer"]:
        if char.isalnum():
            points += 1
    
    total = float(receipt_data["total"])
    if total % 1 == 0:
        points += 50
    if total % 0.25 == 0:
        points += 25

    item_points = (len(receipt_data["items"]) // 2) * 5
    points += item_points

    for item in receipt_data["items"]:
        if len(item["shortDescription"].strip()) % 3 == 0:
            price = float(item["price"])
            points += math.ceil(price * 0.2)

    day = int(receipt_data["purchaseDate"].split("-")[2])
    if day % 2 == 1:
        points += 6

    purchase_time = datetime.strptime(receipt_data["purchaseTime"], "%H:%M").time()
    lower_bound = time(14, 0, 0)
    upper_bound = time(16, 0, 0)

    if lower_bound < purchase_time < upper_bound:
        points += 10

    return points
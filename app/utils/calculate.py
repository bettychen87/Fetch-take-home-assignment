from datetime import datetime, time
import math

def calculate_points(receipt_data):
    """
    Calculate points for a given receipt.

    Args:
        receipt_data (dict): The receipt data in the form of a dictionary.

    Returns:
        int: The total points calculated based on the receipt data.
    """
    # Initialize the points counter to zero.
    points = 0

    # Calculate points based on the retailer name.
    for char in receipt_data["retailer"]:
        if char.isalnum():  # Check if the character is alphanumeric.
            points += 1  # Add 1 point for each alphanumeric character.

    # Calculate points based on the total purchase amount.
    total = float(receipt_data["total"])
    if total % 1 == 0:  # Check if the total amount is an integer.
        points += 50  # Add 50 points for a whole number total.
    if total % 0.25 == 0:  # Check if the total amount is a multiple of 0.25.
        points += 25  # Add 25 points for each 0.25 increment.

    # Calculate points based on the number of items in the receipt.
    item_points = (len(receipt_data["items"]) // 2) * 5
    points += item_points

    # Calculate points for each item based on its description and price.
    for item in receipt_data["items"]:
        if len(item["shortDescription"].strip()) % 3 == 0:
            price = float(item["price"])
            points += math.ceil(price * 0.2)

    # Calculate points based on the purchase date.
    day = int(receipt_data["purchaseDate"].split("-")[2])
    if day % 2 == 1: 
        points += 6  # Add 6 points if the day is odd.

    # Calculate points based on the purchase time.
    purchase_time = datetime.strptime(receipt_data["purchaseTime"], "%H:%M").time()
    lower_bound = time(14, 0, 0)  # Define the lower time boundary (2:00 PM).
    upper_bound = time(16, 0, 0)  # Define the upper time boundary (4:00 PM).

    if lower_bound < purchase_time < upper_bound:
        points += 10  # Add 10 points if the purchase time is within the specified range.

    # Return the total points calculated for the receipt.
    return points

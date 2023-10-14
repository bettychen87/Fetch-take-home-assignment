import datetime
from flask import Flask, request, jsonify
import math
import uuid

app = Flask(__name__)
app.config["DEBUG"] = True

receipts = {}

def calculate_points(receipt_data):
    points = 0
    for char in receipt_data["retailer"]:
        if char.isalnum():
            points += 1
    if receipt_data["total"] % 1 == 0:
        points += 50
    if receipt_data["total"] % 0.25 == 0:
        points += 25
    
    item_points = (len(receipt_data["items"]) // 2) * 5
    points += item_points

    for item in receipt_data["item"]:
        if len(item["description"].strip()) % 3 == 0:
            points += math.ceil(item["price"] * 0.2)

        day = int(item["purchaseDate"].split("-")[2])
        if day % 2 == 1:
            points += 6

        purchase_time = datetime.strptime(item["purchaseTime"], "%H:%M:%S").time()
        lower_bound = datetime.time(14, 0, 0)
        upper_bound = datetime.time(16, 0, 0)

        if lower_bound < purchase_time < upper_bound:
            points += 10

    return points

@app.route('/receipt/process', methods = ['POST'])
def process_receipts():
    receipt_data = request.get_json()
    receipt_id = str(uuid.uuid4())

    receipt_points = calculate_points(receipt_data)
    receipts[receipt_data] = {
        "data": receipt_data,
        "points": receipt_points
    }

    return jsonify({"receipt_id": receipt_id})

@app.route('/receipts/<int:receipt_id>/points', methods = ['GET'])
def get_receipt_points(receipt_id):
    if receipt_id not in receipts:
        return jsonify({"error": "Receipt not found"})
    else:
        receipt_points = receipts[receipt_id]["points"]
        return jsonify({"points": receipt_points})

if __name__ == "__main__":
   app.run(debug = True)

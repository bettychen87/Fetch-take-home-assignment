import datetime
from flask import Flask, request, jsonify
import math
import uuid

app = Flask(__name__)
app.config["DEBUG"] = True

receipts = {} # to keep track of receipts by id

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

    purchase_time = datetime.datetime.strptime(receipt_data["purchaseTime"], "%H:%M").time()
    lower_bound = datetime.time(14, 0, 0)
    upper_bound = datetime.time(16, 0, 0)

    if lower_bound < purchase_time < upper_bound:
        points += 10

    return points

@app.route('/receipts/process', methods=['POST'])
def process_receipts():
    receipt_data = request.get_json()
    receipt_id = str(uuid.uuid4())

    print(receipt_data)
    receipt_points = calculate_points(receipt_data)
    receipts[receipt_id] = {
        "data": receipt_data,
        "points": receipt_points
    }
    return jsonify({"receipt_id": receipt_id})

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_receipt_points(receipt_id):
    print(receipts)

    if receipt_id not in receipts:
        return jsonify({"error": "Receipt not found"}), 404
    else:
        receipt_points = receipts[receipt_id]["points"]
        return jsonify({"points": receipt_points})

if __name__ == "__main__":
   app.run(debug=True)

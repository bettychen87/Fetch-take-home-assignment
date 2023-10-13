from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

receipts = {}

def calculate_points(receipt_data):
    points = 0

    return points

@app.route('receipt/process', methods = ['POST'])
def process_receipts():
    receipt_data = request.get_json()
    receipt_id = #####

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

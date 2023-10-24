import uuid
from flask import jsonify, request
from app.utils.calculate import calculate_points
from app.receipts_manager import receipts_manager
from . import routes

@routes.route('/receipts/process', methods=['POST'])
def process_receipts():
    """
    Processes and calculate points associated with the receipt given
    Expects a JSON payload:
        - retailer: string representing name of retailer
        - purchaseDate: string representing purchase date of items
        - purchaseTime: string representing purchase time of items
        - items: list of dictionaries
            - shortDescription: string representing a description of the item
            - price: string presenting the price of the item
        - total: string representing the total of the purchase

    Returns a JSON response with the generated receipt ID
    
    """
    receipt_data = request.get_json()

    receipt_id = receipts_manager.process_receipt(receipt_data)

    if receipt_id:
        return jsonify({"receipt_id": receipt_id})
    else:
        return jsonify({"error": "Invalid receipt data"}), 400
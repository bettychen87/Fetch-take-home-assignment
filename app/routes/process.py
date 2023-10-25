import uuid
from flask import jsonify, request
from app.utils.calculate import calculate_points
from app.receipts_manager import receipts_manager
from . import routes

@routes.route('/receipts/process', methods=['POST'])
def process_receipts():
    """
    Process a receipt and calculate associated points.

    Expects a JSON payload with the following fields:
    - retailer (str): Name of the retailer.
    - purchaseDate (str): Purchase date of items (e.g., 'YYYY-MM-DD').
    - purchaseTime (str): Purchase time of items (e.g., 'HH:MM').
    - items (list of dictionaries): List of items, each with the following fields:
      - shortDescription (str): Description of the item.
      - price (str): Price of the item.
    - total (str): Total purchase cost.

    Returns a JSON response with the generated receipt ID or an error message.

    Returns:
    - JSON response: A JSON response containing the receipt ID or an error message if the data is invalid.
    """
    # Get the receipt data from the JSON payload.
    receipt_data = request.get_json()

    # Process the receipt and calculate points.
    receipt_id = receipts_manager.process_receipt(receipt_data)

    if receipt_id:
        # If successful, return a JSON response with the receipt ID.
        return jsonify({"receipt_id": receipt_id})
    else:
        # If the receipt data is invalid, return an error response with HTTP status code 400.
        return jsonify({"error": "Invalid receipt data"}), 400

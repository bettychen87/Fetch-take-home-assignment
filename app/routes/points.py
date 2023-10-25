from flask import jsonify
from app.receipts_manager import receipts_manager
from app.routes import routes
from app.models import Receipt

@routes.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_receipt_points(receipt_id):
    """
    Retrieve the points associated with a specific receipt.

    Args:
        receipt_id (str): The unique identifier of the receipt.

    Returns:
        JSON response: A JSON response containing the points of the receipt, or an error message if not found.
    """
    # Check if the receipt ID exists in the receipts.
    if receipt_id not in receipts_manager.receipts:
        # If not found, return an error response with HTTP status code 404.
        return jsonify({"error": "Receipt not found"}), 404
    else:
        # If the receipt is found, retrieve its points and return a JSON response.
        receipt = receipts_manager.receipts[receipt_id]
        receipt_points = receipt.points
        return jsonify({"points": receipt_points})

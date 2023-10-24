from flask import jsonify
from app.receipts_manager import ReceiptsManager
from . import routes

@routes.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_receipt_points(receipt_id):
    """
    Getting the points of the receipt
    
    """
    manager = ReceiptsManager()

    receipt_data = manager.get_receipt_data(receipt_id)

    if receipt_data:
        receipt_points = receipt_data["points"]
        return jsonify({"points": receipt_points})
    else:
        return jsonify({"error": "Receipt not found"}), 404

        
from flask import jsonify
from app.receipts_manager import receipts_manager
from app.routes import routes

@routes.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_receipt_points(receipt_id):
    """
    Getting the points of the receipt
    
    """

    if receipt_id not in receipts_manager.receipts:
        return jsonify({"error": "Receipt not found"}), 404
    else:
        receipt_points = receipts_manager.receipts[receipt_id]["points"]
        return jsonify({"points": receipt_points})
    
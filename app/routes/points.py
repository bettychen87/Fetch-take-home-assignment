from flask import jsonify

from . import routes, receipts

@routes.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_receipt_points(receipt_id):
    """
    Getting the points of the receipt
    
    """

    if not receipts.get(receipt_id):
        return jsonify({"error": "Receipt not found"}), 404
    else:
        receipt_points = receipts[receipt_id]["points"]
        return jsonify({"points": receipt_points})

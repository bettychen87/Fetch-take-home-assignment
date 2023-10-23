import uuid
from flask import jsonify, request
from app.utils import calculate_points
from app.models import receipts

from . import routes, receipts

@routes.route('/receipts/process', methods=['POST'])
def process_receipts():
    receipt_data = request.get_json()
    receipt_id = str(uuid.uuid4())

    receipt_points = calculate_points(receipt_data)
    receipts[receipt_id] = {
        "data": receipt_data,
        "points": receipt_points
    }
    return jsonify({"receipt_id": receipt_id})

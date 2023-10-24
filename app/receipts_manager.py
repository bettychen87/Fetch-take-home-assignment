import uuid
from flask import jsonify
from .utils.data_validator import validate_receipt_data
from .utils.calculate import calculate_points

class ReceiptsManager:
    def __init__(self):
        self.receipts = {}

    def process_receipt(self, receipt_data):
        if validate_receipt_data(receipt_data):
            receipt_id = str(uuid.uuid4())
            receipt_points = calculate_points(receipt_data)
            self.receipts[receipt_id] = {
                "data" : receipt_data,
                "points" : receipt_points
            }
            return receipt_id
        else:
            return jsonify({"error": "Receipt invalid"}), 404

    def get_receipt_data(self, receipt_id: str) -> dict:
        if receipt_id in self.receipts:
            return self.receipts[receipt_id]
        else:
            return jsonify({"error": "Receipt not found"}), 404

receipts_manager = ReceiptsManager()

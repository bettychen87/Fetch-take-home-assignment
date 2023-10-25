import uuid
from flask import jsonify
from .utils.data_validator import validate_receipt_data
from .utils.calculate import calculate_points

class ReceiptsManager:
    def __init__(self):
        """
        Initialize a ReceiptsManager.

        This class manages the processing and storage of receipts and associated points.
        """
        self.receipts = {}

    def process_receipt(self, receipt_data):
        """
        Process a receipt and store it with associated points.

        Args:
            receipt_data (dict): The receipt data containing information about the purchase.

        Returns:
            str: The generated receipt ID if processing is successful, or None if the data is invalid.
        """
        if validate_receipt_data(receipt_data):
            # Generate a unique receipt ID.
            receipt_id = str(uuid.uuid4())

            # Calculate points associated with the receipt.
            receipt_points = calculate_points(receipt_data)

            # Store the receipt and associated points.
            self.receipts[receipt_id] = {
                "data": receipt_data,
                "points": receipt_points
            }

            return receipt_id
        else:
            # Return error if the receipt data is invalid.
            return jsonify({"error": "Invalid receipt data"}), 400

    def get_receipt_data(self, receipt_id: str) -> dict:
        """
        Retrieve receipt data by its ID.

        Args:
            receipt_id (str): The unique receipt ID.

        Returns:
            dict: The receipt data associated with the given receipt ID.
        """
        if receipt_id in self.receipts:
            return self.receipts[receipt_id]
        else:
            # If the receipt ID is not found, return an error response with HTTP status code 404.
            return jsonify({"error": "Receipt not found"}), 404

# Create an instance of ReceiptsManager to manage receipts and points.
receipts_manager = ReceiptsManager()

import unittest
from app import create_app
from app.receipts_manager import ReceiptsManager

class TestReceiptsProcessing(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.app = create_app().test_client()

        # Create an instance of ReceiptsManager
        self.manager = ReceiptsManager()

    def test_processing(self):
        # Define test data for processing a receipt
        data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                    "shortDescription": "Mountain Dew 12PK",
                    "price": "6.49"
                },
                {
                    "shortDescription": "Emils Cheese Pizza",
                    "price": "12.25"
                },
                {
                    "shortDescription": "Knorr Creamy Chicken",
                    "price": "1.26"
                },
                {
                    "shortDescription": "Doritos Nacho Cheese",
                    "price": "3.35"
                },
                {
                    "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                    "price": "12.00"
                }
            ],
            "total": "35.35"
        }

        # Send a POST request to process the receipt
        response = self.app.post('/receipts/process', json=data)
        json_data = response.get_json()

        # Check if the response is successful and contains receipt_id
        self.assertEqual(response.status_code, 200)
        self.assertIn("receipt_id", json_data)

        # Capture the generated receipt_id for testing
        self.receipt_id = json_data["receipt_id"]

if __name__ == '__main__':
    unittest.main()

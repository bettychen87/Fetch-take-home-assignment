import unittest
from app import create_app
from app.receipts_manager import ReceiptsManager

class TestGetReceiptPoints(unittest.TestCase):
    def setUp(self):
        # Create a test client for the Flask app
        self.app = create_app().test_client()

        # Create an instance of ReceiptsManager
        self.manager = ReceiptsManager()

        # Process a receipt to get a receipt_id for testing
        data = {
            "retailer": "Test Retailer",
            "purchaseDate": "2023-10-15",
            "purchaseTime": "15:30",
            "items": [
                {
                    "shortDescription": "Item 1",
                    "price": "10.99"
                },
                {
                    "shortDescription": "Item 2",
                    "price": "5.99"
                }
            ],
            "total": "16.98"
        }
        response = self.app.post('/receipts/process', json=data)
        json_data = response.get_json()
        self.receipt_id = json_data["receipt_id"]  # Capture the receipt_id

    def test_getting_points(self):
        # Use self.receipt_id in your test to retrieve receipt points
        response = self.app.get(f'/receipts/{self.receipt_id}/points')
        json_data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("points", json_data)
    
    def tearDown(self):
        # Clean up by removing the test receipt after the test is done
        if self.receipt_id in self.manager.receipts:
            del self.manager.receipts[self.receipt_id]

if __name__ == '__main__':
    unittest.main()

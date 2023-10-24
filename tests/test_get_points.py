import unittest
from app import create_app
from app.receipts_manager import ReceiptsManager

class TestGetReceiptPoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
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
        # Now you can use self.receipt_id in your test
        response = self.app.get(f'/receipts/{self.receipt_id}/points')
        json_data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("points", json_data)

if __name__ == '__main__':
    unittest.main()
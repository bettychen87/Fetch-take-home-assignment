import unittest
from app import create_app
from app.receipts_manager import ReceiptsManager

class TestReceiptsProcessing(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.manager = ReceiptsManager()

    def test_processing(self):
        data = {
                "retailer": "Target",
                "purchaseDate": "2022-01-01",
                "purchaseTime": "13:01",
                "items": [
                    {
                    "shortDescription": "Mountain Dew 12PK",
                    "price": "6.49"
                    },{
                    "shortDescription": "Emils Cheese Pizza",
                    "price": "12.25"
                    },{
                    "shortDescription": "Knorr Creamy Chicken",
                    "price": "1.26"
                    },{
                    "shortDescription": "Doritos Nacho Cheese",
                    "price": "3.35"
                    },{
                    "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                    "price": "12.00"
                    }
                ],
                "total": "35.35"
                }
        response = self.app.post('/receipts/process', json=data)
        json_data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn("receipt_id", json_data)
        self.receipt_id = json_data["receipt_id"]  # Capture the receipt_id


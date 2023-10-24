import json
from app import create_app, receipts

app = create_app()

def test_points():
    receipts = app.test_client()

    

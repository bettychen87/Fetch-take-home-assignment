class Receipt:
    def __init__(self, receipt_id, retailer, purchase_date, purchase_time, items, total, points):
        """
        Initialize a Receipt object.

        Args:
            receipt_id (str): Unique identifier for the receipt.
            retailer (str): Name of the retailer.
            purchase_date (str): Purchase date in 'YYYY-MM-DD' format.
            purchase_time (str): Purchase time in 'HH:MM' format.
            items (list of dict): List of items, each with 'shortDescription' and 'price'.
            total (float): Total purchase cost.
            points (int): Points associated with the receipt.
        """
        self.receipt_id = receipt_id
        self.retailer = retailer
        self.purchase_date = purchase_date
        self.purchase_time = purchase_time
        self.items = items
        self.total = total
        self.points = points

    def to_dict(self):
        """
        Convert the Receipt object to a dictionary.

        Returns:
            dict: Dictionary representation of the Receipt object.
        """
        return {
            "receipt_id": self.receipt_id,
            "retailer": self.retailer,
            "purchase_date": self.purchase_date,
            "purchase_time": self.purchase_time,
            "items": self.items,
            "total": self.total,
            "points": self.points
        }

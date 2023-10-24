import unittest
from tests.test_get_points import TestGetReceiptPoints
from tests.test_process_receipt import TestReceiptsProcessing

if __name__ == "__main__":
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestGetReceiptPoints))
    test_suite.addTest(test_loader.loadTestsFromTestCase(TestReceiptsProcessing))

    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

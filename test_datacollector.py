import unittest
from data_collector import valid_identity


class TestUtils(unittest.TestCase):
    
    def test_valid_identity(self):
        result = test_valid_identity('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
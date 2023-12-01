import unittest
from data_collector import valid_identity


class TestUtils(unittest.TestCase):
    
    def test_valid_identity(self):
        # Test for a name 32 characters long
        result = valid_identity('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
        self.assertEqual(result, True)
        
        # Test for a name more than 32 characters long
        result = valid_identity('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB')
        self.assertEqual(result, False)
        
        # TODO: add the other tests for a valid name (illegal characters, etc)
        


if __name__ == '__main__':
    unittest.main()

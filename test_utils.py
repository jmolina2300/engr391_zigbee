import unittest
from utils import read_last_n_lines
from utils import file_exists


class TestUtils(unittest.TestCase):

    def test_read_last_n_lines(self):
        with open('test_data.txt', 'rb') as f:
            lines = read_last_n_lines(f,10)
            self.assertEqual(len(lines), 10)
        
        with open('test_data.txt', 'rb') as f:
            lines = read_last_n_lines(f,20)
            self.assertEqual(len(lines), 20)
        
        with open('test_data.txt', 'rb') as f:
            lines = read_last_n_lines(f,80)
            self.assertEqual(len(lines), 80)
            
        # Edge case where we read 1 extra line
        #with open('test_data.txt', 'rb') as f:
        #    lines = read_last_n_lines(f,81)
        #    self.assertEqual(len(lines), 80)
        
        # Edge case where we read only 1 line
        with open('test_data.txt', 'rb') as f:
            lines = read_last_n_lines(f,1)
            self.assertEqual(len(lines), 1)
    
    def test_file_exsists(self):
        result = file_exists('FileThatDoesntExist')
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
import unittest

class TestExample(unittest.TestCase):
    def test_1(self):
        self.assertEqual('rohit','rohit')

if __name__=='__main__':
    unittest.main()
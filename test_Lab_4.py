import unittest
import Lab_4

class test_Lab_4(unittest.TestCase):
    def test_squared(self):
        self.assertEqual(Lab_4.squared(5), [1,4,9,16,25])
        
    def test_cubed(self):
        self.assertEqual(Lab_4.cubed(5), [1,8,27,64,125])

if __name__ == '__main__':
    unittest.main()

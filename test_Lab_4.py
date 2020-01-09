import unittest
import Lab_4

class test_Lab_4(unittest.TestCase):
    def test_squared(self):
        self.assertEqual(Lab_4.squared(5), [1,4,9,16,25])
        self.assertEqual(Lab_4.squared(10), [1,4,9,16,25, 36, 49, 64, 81, 100])
        self.assertEqual(Lab_4.squared(6), [1,4,9,16,25, 36])
        self.assertEqual(Lab_4.squared(3), [1,4,9])
        self.assertEqual(Lab_4.squared(8), [1,4,9,16,25, 36, 49, 64])
        
    def test_cubed(self):
        self.assertEqual(Lab_4.cubed(5), [1,8,27,64,125])
        self.assertEqual(Lab_4.cubed(10), [1,8,27,64,125, 216, 343, 512, 729, 1000])
        self.assertEqual(Lab_4.cubed(6), [1,8,27,64,125, 216])
        self.assertEqual(Lab_4.cubed(3), [1,8,27])
        self.assertEqual(Lab_4.cubed(8), [1,8,27,64,125, 216, 343, 512])

if __name__ == '__main__':
    unittest.main()

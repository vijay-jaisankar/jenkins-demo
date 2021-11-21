import unittest
from compute_average import compute_average_function

"""
    Test cases for the compute_average() function
"""
class TestAverage(unittest.TestCase):

    def setUp(self):
        pass

    def testEmptyList(self):
        self.assertEqual(compute_average_function([]),0.0)
    
    def testOnlyPositive(self):
        self.assertEqual(compute_average_function([1,2,3]),2.0)

    def testOnlyNegative(self):
        self.assertEqual(compute_average_function([-1,-2,-3]),-2.0)
    
    def testSumZero(self):
        self.assertEqual(compute_average_function([-1,1]),0.0)

    def testIncorrectType(self):
        with self.assertRaises(TypeError):
            compute_average_function(["A","B","C"])

if __name__ == "__main__":
    unittest.main()

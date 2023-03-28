import unittest
from code_Assignment1 import convertInchToMeter
from code_Assignment1 import convertPoundsToKilos

class Test_Conversions(unittest.TestCase):

    def test_convertInchToMeter_Equal(self):
        #result = convertInchToMeter(72)
        #self.assertEqual(result, 1.8288)
        self.assertEqual(convertInchToMeter(72), 1.8288)

    def test_convertInchToMeter_NotEqual(self):
        #result = convertInchToMeter(72)
        #self.assertNotEqual(result, 42)
        self.assertNotEqual(convertInchToMeter(72), 42)

    def test_convertPoundsToKilos_Equal(self):
        #result = convertPoundsToKilos(275)
        #self.assertEqual(result, 124.7125)
        self.assertEqual(convertPoundsToKilos(275), 124.7125)

    def test_convertPoundsToKilos_NotEqual(self):
        #result = convertPoundsToKilos(275)
        #self.assertNotEqual(result, 42)
        self.assertNotEqual(convertPoundsToKilos(275), 42)

if __name__ == '__main__':
    unittest.main()

# run tests using:
# $python test_Assignment1_2.py 
# ....
# ----------------------------------------------------------------------
# Ran 4 tests in 0.000s

# OK
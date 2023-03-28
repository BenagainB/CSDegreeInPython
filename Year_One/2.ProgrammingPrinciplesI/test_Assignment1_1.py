import unittest

class Test_Conversions(unittest.TestCase):

    def test_convertInchToMeter(self):
        result = 72 * 0.0254
        self.assertEqual(result, 1.8288)
    
    def test_convertPoundsToKilos(self):
        result = 275 * 0.4535
        self.assertEqual(result, 124.7125)


# run tests using:
# $python -m unittest test_Assignment1_1.py
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
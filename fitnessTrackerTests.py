# Project 1 Fitness Tracking Tests
# At least 2 tests for each function
#
# Name: Tyler Baxter
# Section: 03
# Date: 01/14/22

import unittest
from fitnessTrackerFuncs import *


class MyTestCase(unittest.TestCase):
    def test_convert_lb_to_kg(self):
        self.assertEqual(convert_lb_to_kg(0), 0)
        self.assertEqual(convert_lb_to_kg(1), 0.45359237)
        self.assertEqual(convert_lb_to_kg(50), 22.6796185)

    def test_compute_MET(self):
        self.assertEqual(compute_MET(1), 5)
        self.assertEqual(compute_MET(2), 7)
        self.assertEqual(compute_MET(3), 3)
        self.assertEqual(compute_MET(4), 4)

    def test_compute_calorie_burned(self):
        self.assertEqual(compute_calorie_burned(100, 100, 1), 175)
        self.assertEqual(compute_calorie_burned(80, 150, 2), 420)
        self.assertEqual(compute_calorie_burned(60, 200, 3), 630)
        self.assertEqual(compute_calorie_burned(40, 250, 4), 700)
        self.assertEqual(compute_calorie_burned(88, 127, 3), 586.74)

    def test_compute_bmi(self):
        self.assertEqual(compute_BMI(100, 100), 7.03)
        self.assertAlmostEqual(compute_BMI(180, 70), 25.82448979)
        self.assertAlmostEqual(compute_BMI(193, 65), 32.11337278)

    def test_compute_bmi_category(self):
        self.assertEqual(BMI_category(18), "Underweight")
        self.assertEqual(BMI_category(24.5), "Normal weight")
        self.assertEqual(BMI_category(25.5), "Overweight")
        self.assertEqual(BMI_category(100), "Obesity")

    def test_compute_equivalent_miles(self):
        self.assertAlmostEqual(compute_equivalent_miles(65, 2, 100), 9.61776357)
        self.assertAlmostEqual(compute_equivalent_miles(55, 1, 50), 2.15104166)
        self.assertAlmostEqual(compute_equivalent_miles(50, 4, 200), 9.90782828)


if __name__ == '__main__':
    unittest.main()

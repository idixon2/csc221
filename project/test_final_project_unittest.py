import unittest
from final_project import (
    is_leap_year
)

class TestFinal(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(1996))
        self.assertFalse(is_leap_year(1990))
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2000))








if __name__ == '__main__':
    unittest.main()
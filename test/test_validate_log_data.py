import unittest
import fair_billing


class UnitTest(unittest.TestCase):

    def setUp(self):
        self.log_line1 = "11:00:11 kelvin Start"
        self.log_line2 = "14:11:11 kelvin End"
        self.log_line3 = "12:20:22 kelvin"
        self.log_line4 = "12:20:11 End"
        self.log_line5 = "kelvin Start"
        self.positive = True
        self.negative = False

    def test_validate1(self):
        self.assertEqual(fair_billing.validate_log_entry(self.log_line1), self.positive)

    def test_validate2(self):
        self.assertEqual(fair_billing.validate_log_entry(self.log_line2), self.positive)

    def test_validate3(self):
        self.assertEqual(fair_billing.validate_log_entry(self.log_line3), self.negative)

    def test_validate4(self):
        self.assertEqual(fair_billing.validate_log_entry(self.log_line4), self.negative)

    def test_validate5(self):
        self.assertEqual(fair_billing.validate_log_entry(self.log_line5), self.negative)


if __name__ == "__main__":
    unittest.main()

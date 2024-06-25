import unittest
import fair_billing


class UnitTest(unittest.TestCase):

    def setUp(self):
        self.username = "kelvin"
        self.seconds = 60
        self.data = {
            "kelvin": {"sessions": 2, "total_seconds": 60},
            "dave": {"sessions": 4, "total_seconds": 120},
        }
        self.results = {
            "kelvin": {"sessions": 3, "total_seconds": 120},
            "dave": {"sessions": 4, "total_seconds": 120},
        }

    def test_update_data(self):
        self.assertEqual(
            fair_billing.update_user_data(self.username, self.seconds, self.data),
            self.results,
        )


if __name__ == "__main__":
    unittest.main()

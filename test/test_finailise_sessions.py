import unittest
import fair_billing


class UnitTest(unittest.TestCase):

    def setUp(self):
        self.data = {
            "kelvin": {"sessions": 2, "total_seconds": 60},
            "dave": {"sessions": 4, "total_seconds": 120},
        }
        self.stack = {"kelvin": ["14:55:22"], "dave": ["14:56:22", "14:57:22"]}
        self.end_time = "14:58:22"
        self.time_format = "%H:%M:%S"
        self.results = {
            "kelvin": {"sessions": 3, "total_seconds": 240},
            "dave": {"sessions": 6, "total_seconds": 300},
        }

    def test_stack_cleanout(self):
        self.assertEqual(
            fair_billing.finalize_sessions(
                self.stack, self.end_time, self.data, self.time_format
            ),
            self.results,
        )


if __name__ == "__main__":
    unittest.main()

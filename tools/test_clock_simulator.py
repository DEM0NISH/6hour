"""Unit tests for the exercise clock calculator."""

import unittest
from datetime import datetime

from clock_simulator import deadlines, format_table


class DeadlineTests(unittest.TestCase):
    def test_deadline_offsets(self):
        start = datetime(2026, 11, 7, 2, 40)
        rows = deadlines(start, 24)
        self.assertEqual(rows[0][1], datetime(2026, 11, 7, 8, 40))
        self.assertEqual(rows[1][1], datetime(2026, 11, 8, 2, 40))
        self.assertEqual(rows[2][1], datetime(2026, 11, 10, 2, 40))

    def test_custom_contract_hours(self):
        start = datetime(2026, 1, 1, 0, 0)
        self.assertEqual(deadlines(start, 12)[1][1], datetime(2026, 1, 1, 12, 0))

    def test_past_deadline_warning(self):
        result = format_table(deadlines(datetime(2026, 1, 1), 24), datetime(2026, 1, 2))
        self.assertIn("PAST", result)


if __name__ == "__main__":
    unittest.main()

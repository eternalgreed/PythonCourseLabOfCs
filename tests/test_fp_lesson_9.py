import io
import unittest
from contextlib import redirect_stdout

from fp_lesson_9 import main, odometer


class OdometerTest(unittest.TestCase):
    def test_task_example_returns_thirty_kilometers(self):
        self.assertEqual(odometer([10, 1, 20, 2]), 30)

    def test_theory_example_returns_ninety_kilometers(self):
        self.assertEqual(odometer([15, 1, 25, 2, 30, 3, 10, 5]), 90)

    def test_single_segment_uses_time_from_trip_start(self):
        self.assertEqual(odometer([60, 2]), 120)

    def test_uses_difference_between_cumulative_times(self):
        self.assertEqual(odometer([10, 1, 20, 3]), 50)

    def test_zero_speed_segment_adds_no_distance(self):
        self.assertEqual(odometer([0, 2, 30, 3]), 30)

    def test_input_list_is_not_changed(self):
        oksana = [10, 1, 20, 2]

        odometer(oksana)

        self.assertEqual(oksana, [10, 1, 20, 2])

    def test_main_prints_task_example_result(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertEqual(
            output.getvalue().strip(),
            "Пройденное расстояние: 30 км",
        )


if __name__ == "__main__":
    unittest.main()

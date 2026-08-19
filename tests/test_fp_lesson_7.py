import io
import unittest
from contextlib import redirect_stdout

from fp_lesson_7 import conquest_campaign, main


class ConquestCampaignTest(unittest.TestCase):
    def test_example_is_completed_on_day_three(self):
        result = conquest_campaign(3, 4, 2, [2, 2, 3, 4])

        self.assertEqual(result, 3)

    def test_fully_occupied_field_is_completed_on_first_day(self):
        result = conquest_campaign(1, 1, 1, [1, 1])

        self.assertEqual(result, 1)

    def test_duplicate_landing_coordinates_count_as_one_area(self):
        result = conquest_campaign(2, 2, 2, [1, 1, 1, 1])

        self.assertEqual(result, 3)

    def test_areas_are_captured_only_from_four_sides(self):
        result = conquest_campaign(3, 3, 1, [2, 2])

        self.assertEqual(result, 3)

    def test_long_field_is_not_limited_by_python_recursion_depth(self):
        result = conquest_campaign(1, 1000, 1, [1, 1])

        self.assertEqual(result, 1000)

    def test_only_first_l_landing_coordinates_are_used(self):
        result = conquest_campaign(1, 3, 1, [1, 1, 1, 3])

        self.assertEqual(result, 3)

    def test_input_coordinates_are_not_changed(self):
        battalion = [2, 2, 3, 4]

        conquest_campaign(3, 4, 2, battalion)

        self.assertEqual(battalion, [2, 2, 3, 4])

    def test_main_prints_example_result(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertEqual(
            output.getvalue().strip(),
            "Полигон будет полностью захвачен на день: 3",
        )


if __name__ == "__main__":
    unittest.main()

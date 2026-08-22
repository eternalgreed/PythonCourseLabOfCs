import io
import unittest
from contextlib import redirect_stdout

from fp_lesson_8 import main, second_max


class SecondMaximumTest(unittest.TestCase):
    def test_task_example_counts_duplicate_maximum(self):
        self.assertEqual(second_max([5, 4, 3, 2, 5]), 5)

    def test_returns_second_number_in_descending_order(self):
        self.assertEqual(second_max([9, 4, 7, 2]), 7)

    def test_new_largest_number_moves_previous_largest_to_second_place(self):
        self.assertEqual(second_max([1, 2, 3]), 2)

    def test_works_when_first_number_is_smaller(self):
        self.assertEqual(second_max([2, 8]), 2)

    def test_works_with_negative_numbers(self):
        self.assertEqual(second_max([-10, -3, -7, -4]), -4)

    def test_equal_numbers_can_take_both_first_places(self):
        self.assertEqual(second_max([6, 6, 6]), 6)

    def test_single_number_raises_value_error(self):
        with self.assertRaisesRegex(
            ValueError,
            "Для поиска второго максимума нужны минимум два числа",
        ):
            second_max([5])

    def test_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            second_max([])

    def test_input_list_is_not_changed(self):
        numbers = [5, 4, 3, 2, 5]

        second_max(numbers)

        self.assertEqual(numbers, [5, 4, 3, 2, 5])

    def test_main_prints_task_example_result(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertEqual(
            output.getvalue().strip(),
            "Второе максимальное число: 5",
        )


if __name__ == "__main__":
    unittest.main()

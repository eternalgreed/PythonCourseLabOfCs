import io
import importlib
import unittest
from contextlib import redirect_stdout

from pymonad.maybe import Just, Nothing

import fp_lesson_5
from fp_lesson_5 import banana, begin, main, show, to_left, to_right


class TightropeLessonTest(unittest.TestCase):
    def test_begin_returns_empty_balanced_pole(self):
        self.assertEqual(begin(), Just([0, 0]))

    def test_to_left_returns_new_state_without_mutating_input(self):
        pole = [0, 0]

        result = to_left(2)(pole)

        self.assertEqual(result, Just([2, 0]))
        self.assertEqual(pole, [0, 0])

    def test_to_right_returns_new_state_without_mutating_input(self):
        pole = [2, 0]

        result = to_right(5)(pole)

        self.assertEqual(result, Just([2, 5]))
        self.assertEqual(pole, [2, 0])

    def test_to_right_allows_birds_to_fly_away(self):
        self.assertEqual(to_right(-2)([1, 3]), Just([1, 1]))

    def test_difference_of_exactly_four_keeps_balance(self):
        self.assertEqual(to_right(4)([0, 0]), Just([0, 4]))

    def test_difference_greater_than_four_returns_nothing(self):
        self.assertEqual(to_left(5)([0, 0]), Nothing)
        self.assertEqual(to_right(5)([0, 0]), Nothing)

    def test_banana_always_returns_nothing(self):
        self.assertEqual(banana([2, 0]), Nothing)

    def test_three_article_chains_have_expected_results(self):
        imbalance = (
            begin()
            .bind(to_left(2))
            .bind(to_right(5))
            .bind(to_left(-2))
        )
        balanced = (
            begin()
            .bind(to_left(2))
            .bind(to_right(5))
            .bind(to_left(-1))
        )
        slipped = (
            begin()
            .bind(to_left(2))
            .bind(banana)
            .bind(to_right(5))
            .bind(to_left(-1))
        )

        self.assertEqual(imbalance, Nothing)
        self.assertEqual(balanced, Just([1, 5]))
        self.assertEqual(slipped, Nothing)

    def test_show_prints_status_and_successful_state(self):
        output = io.StringIO()

        with redirect_stdout(output):
            show(Nothing)
            show(Just([1, 5]))

        self.assertEqual(output.getvalue().splitlines(), [
            "False",
            "True: [1, 5]",
        ])

    def test_main_prints_all_three_article_results(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()

        self.assertEqual(output.getvalue().splitlines(), [
            "False",
            "True: [1, 5]",
            "False",
        ])

    def test_import_does_not_print_anything(self):
        output = io.StringIO()

        with redirect_stdout(output):
            importlib.reload(fp_lesson_5)

        self.assertEqual(output.getvalue(), "")


if __name__ == "__main__":
    unittest.main()

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import call, patch

from console_lesson import create_summary, main


class ConsoleLessonTest(unittest.TestCase):
    def test_create_summary(self):
        summary = create_summary("Алексей", "Москва", 25)

        self.assertEqual(summary, [
            "Здравствуйте, Алексей!",
            "Ваш город: Москва",
            "Ваш возраст: 25",
            "Через год ваш возраст будет: 26",
        ])

    def test_main_repeats_input_after_invalid_age(self):
        output = io.StringIO()

        with patch(
            "builtins.input",
            side_effect=["Алексей", "Москва", "не число", "25"],
        ) as input_mock, redirect_stdout(output):
            main()

        input_mock.assert_has_calls([
            call("Введите ваше имя: "),
            call("Введите ваш город: "),
            call("Введите ваш возраст: "),
            call("Введите ваш возраст: "),
        ])
        self.assertIn(
            "Ошибка: возраст нужно ввести целым числом.",
            output.getvalue(),
        )
        self.assertIn("Здравствуйте, Алексей!", output.getvalue())
        self.assertIn("Через год ваш возраст будет: 26", output.getvalue())


if __name__ == "__main__":
    unittest.main()

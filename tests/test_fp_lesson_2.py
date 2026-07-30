import unittest

from fp_lesson_2 import concatenate, first_step, hello, make_greeting


class CurryingLessonTest(unittest.TestCase):
    def test_concatenate_joins_two_strings(self):
        self.assertEqual(
            concatenate("functional ", "programming"),
            "functional programming",
        )

    def test_hello_accepts_only_name(self):
        self.assertEqual(hello("Petya"), "Hello, Petya")

    def test_first_step_matches_task_example(self):
        final = first_step("Hello")(",")("!")

        self.assertEqual(final("Petya"), "Hello, Petya!")

    def test_configured_greeting_can_be_reused(self):
        final = first_step("Hello")(",")("!")

        self.assertEqual(final("Anna"), "Hello, Anna!")
        self.assertEqual(final("Ivan"), "Hello, Ivan!")

    def test_another_greeting_can_be_configured(self):
        final = make_greeting("Привет")(",")("!")

        self.assertEqual(final("Маша"), "Привет, Маша!")


if __name__ == "__main__":
    unittest.main()

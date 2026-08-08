import unittest

from pymonad.list import ListMonad
from pymonad.maybe import Just

from fp_lesson_4 import add, add10


class FunctorLessonTest(unittest.TestCase):
    def test_add_can_be_partially_applied(self):
        add_ten = add(10)

        self.assertEqual(add_ten(5), 15)

    def test_add10_adds_ten_to_just(self):
        self.assertEqual(add10(Just(5)), Just(15))

    def test_add10_preserves_just_type(self):
        source = Just(5)
        result = add10(source)

        self.assertIs(type(result), type(source))

    def test_add10_adds_ten_to_list_monad(self):
        self.assertEqual(
            add10(ListMonad(1, 2, 3)),
            ListMonad(11, 12, 13),
        )

    def test_add10_preserves_list_monad_type(self):
        source = ListMonad(1, 2, 3)
        result = add10(source)

        self.assertIs(type(result), type(source))


if __name__ == "__main__":
    unittest.main()

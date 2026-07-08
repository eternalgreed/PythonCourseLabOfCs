import unittest

from oop_lesson_1 import (
    Hero,
    Monster,
    Weapon,
    create_demo_world,
    demonstrate_reference_effect,
)


class OopLessonOneTest(unittest.TestCase):
    def test_creates_related_game_objects(self):
        hero, sword, monster = create_demo_world()

        self.assertIsInstance(hero, Hero)
        self.assertIsInstance(sword, Weapon)
        self.assertIsInstance(monster, Monster)
        self.assertEqual(hero.weapon, sword)
        self.assertEqual(monster.target, hero)

    def test_demonstrates_reference_side_effect(self):
        before_level, after_level, same_object = demonstrate_reference_effect()

        self.assertEqual(before_level, 3)
        self.assertEqual(after_level, 4)
        self.assertTrue(same_object)


if __name__ == "__main__":
    unittest.main()

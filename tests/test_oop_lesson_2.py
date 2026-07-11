import unittest

from oop_lesson_2 import Hero, Weapon


class OopLessonTwoTest(unittest.TestCase):
    def test_weapon_power_depends_on_durability(self):
        weapon = Weapon("Iron Sword", 20, 50, 3.5)

        self.assertEqual(weapon.get_power(), 10)

    def test_hero_attack_uses_equipped_weapon(self):
        hero = Hero("Artem", "Knight", 3, 100)
        weapon = Weapon("Iron Sword", 20, 100, 3.5)
        hero.equip_weapon(weapon)

        self.assertEqual(hero.attack(), 26)
        self.assertEqual(weapon.durability, 90)

    def test_hero_heal_cannot_exceed_max_health(self):
        hero = Hero("Artem", "Knight", 3, 80)

        hero.heal(50)

        self.assertEqual(hero.health, 100)


if __name__ == "__main__":
    unittest.main()

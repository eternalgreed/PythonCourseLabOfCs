class Weapon:
    def __init__(self, title, damage, durability, weight):
        self.title = title
        self.damage = damage
        self.durability = durability
        self.weight = weight

    def get_power(self):
        return int(self.damage * self.durability / 100)

    def use(self):
        if self.durability > 0:
            self.durability -= 10

        if self.durability < 0:
            self.durability = 0

    def repair(self, points):
        self.durability += points

        if self.durability > 100:
            self.durability = 100

    def is_broken(self):
        return self.durability == 0


class Hero:
    def __init__(self, name, game_class, level, health):
        self.name = name
        self.game_class = game_class
        self.level = level
        self.health = health
        self.max_health = 100
        self.weapon = None

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        base_damage = self.level * 2

        if self.weapon is None:
            return base_damage

        damage = base_damage + self.weapon.get_power()
        self.weapon.use()

        return damage

    def heal(self, points):
        self.health += points

        if self.health > self.max_health:
            self.health = self.max_health

    def is_alive(self):
        return self.health > 0


def print_weapon(weapon):
    print("Weapon:", weapon.title)
    print("Damage:", weapon.damage)
    print("Durability:", weapon.durability)
    print("Weight:", weapon.weight)
    print("Current power:", weapon.get_power())
    print("Broken:", weapon.is_broken())
    print()


def print_hero(hero):
    print("Hero:", hero.name)
    print("Class:", hero.game_class)
    print("Level:", hero.level)
    print("Health:", hero.health)
    print("Alive:", hero.is_alive())

    if hero.weapon is None:
        print("Weapon: no weapon")
    else:
        print("Weapon:", hero.weapon.title)

    print()


def main():
    hero = Hero("Artem", "Knight", 3, 80)
    sword = Weapon("Iron Sword", 20, 100, 3.5)
    axe = Weapon("Heavy Axe", 30, 70, 6.0)

    print("Initial objects")
    print_hero(hero)
    print_weapon(sword)
    print_weapon(axe)

    hero.equip_weapon(sword)
    print("After equip_weapon")
    print_hero(hero)

    first_attack_damage = hero.attack()
    second_attack_damage = hero.attack()
    print("Attack results")
    print("First attack damage:", first_attack_damage)
    print("Second attack damage:", second_attack_damage)
    print("Sword durability after attacks:", sword.durability)
    print()

    hero.heal(50)
    sword.repair(15)

    print("After heal and repair")
    print_hero(hero)
    print_weapon(sword)


if __name__ == "__main__":
    main()

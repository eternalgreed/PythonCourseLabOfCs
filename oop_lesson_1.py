class Hero:
    name = ""
    game_class = ""
    level = 1
    health = 100
    mana = 50
    location = ""
    weapon = None


class Weapon:
    title = ""
    damage = 0
    weapon_type = ""
    weight = 0.0
    durability = 100
    rarity = ""


class Monster:
    name = ""
    species = ""
    health = 100
    damage = 10
    location = ""
    aggression = 0
    target = None


def create_demo_world():
    hero = Hero()
    hero.name = "Artem"
    hero.game_class = "Knight"
    hero.level = 3
    hero.health = 120
    hero.mana = 25
    hero.location = "Old Forest"

    sword = Weapon()
    sword.title = "Iron Sword"
    sword.damage = 18
    sword.weapon_type = "Sword"
    sword.weight = 3.5
    sword.durability = 80
    sword.rarity = "Common"

    monster = Monster()
    monster.name = "Forest Bandit"
    monster.species = "Bandit"
    monster.health = 65
    monster.damage = 9
    monster.location = "Old Forest"
    monster.aggression = 7

    hero.weapon = sword
    monster.target = hero

    return hero, sword, monster


def print_hero(hero):
    print("Hero")
    print("Name:", hero.name)
    print("Class:", hero.game_class)
    print("Level:", hero.level)
    print("Health:", hero.health)
    print("Mana:", hero.mana)
    print("Location:", hero.location)
    print("Weapon:", hero.weapon.title)
    print()


def print_weapon(weapon):
    print("Weapon")
    print("Title:", weapon.title)
    print("Damage:", weapon.damage)
    print("Type:", weapon.weapon_type)
    print("Weight:", weapon.weight)
    print("Durability:", weapon.durability)
    print("Rarity:", weapon.rarity)
    print()


def print_monster(monster):
    print("Monster")
    print("Name:", monster.name)
    print("Species:", monster.species)
    print("Health:", monster.health)
    print("Damage:", monster.damage)
    print("Location:", monster.location)
    print("Aggression:", monster.aggression)
    print("Target:", monster.target.name)
    print()


def demonstrate_reference_effect():
    hero, sword, monster = create_demo_world()
    same_hero = hero

    before_level = hero.level
    same_hero.level = 4
    after_level = hero.level

    return before_level, after_level, hero is same_hero


def print_reference_effect():
    hero, sword, monster = create_demo_world()
    same_hero = hero

    print("Reference effect example")
    print("hero.level before change:", hero.level)

    same_hero.level = 4

    print("same_hero.level after change:", same_hero.level)
    print("hero.level after change:", hero.level)
    print("hero is same_hero:", hero is same_hero)
    print()


def main():
    hero, sword, monster = create_demo_world()

    print_hero(hero)
    print_weapon(sword)
    print_monster(monster)
    print_reference_effect()


if __name__ == "__main__":
    main()

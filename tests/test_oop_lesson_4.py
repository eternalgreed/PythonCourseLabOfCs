import io
import random
import unittest
from contextlib import redirect_stdout

from oop_lesson_4 import (
    Bird,
    Cat,
    CityCar,
    DeliveryVan,
    ElectricEngine,
    GasolineEngine,
    fill_animals,
)


class OopLessonFourTest(unittest.TestCase):
    def test_vehicle_uses_composed_engine(self):
        engine = GasolineEngine("G-100", 120, 20)
        car = CityCar("Lada", "Vesta", engine, 480)

        self.assertTrue(car.drive(30))
        self.assertEqual(car.get_mileage(), 30)
        self.assertEqual(engine.get_fuel_level(), 17)
        self.assertEqual(car.get_engine_model(), "G-100")

    def test_different_vehicle_and_engine_children_work_together(self):
        engine = ElectricEngine("E-200", 90, 80)
        van = DeliveryVan("GAZ", "Sobol", engine, 900)

        self.assertTrue(van.load_cargo(350))
        self.assertTrue(van.drive(50))
        self.assertEqual(van.get_mileage(), 50)
        self.assertEqual(engine.get_battery_charge(), 70)

    def test_fill_animals_clears_and_fills_existing_list(self):
        animals = [Cat()]
        original_list_id = id(animals)
        random.seed(10)

        fill_animals(animals)

        self.assertEqual(id(animals), original_list_id)
        self.assertEqual(len(animals), 500)
        self.assertEqual(sum(isinstance(animal, Cat) for animal in animals), 250)
        self.assertEqual(sum(isinstance(animal, Bird) for animal in animals), 250)
        self.assertEqual(len({id(animal) for animal in animals}), 500)

    def test_polymorphic_foo_calls_child_methods(self):
        output = io.StringIO()

        with redirect_stdout(output):
            for animal in [Cat(), Bird()]:
                animal.foo()

        self.assertEqual(output.getvalue().splitlines(), [
            "Кошка мурлычет",
            "Птица поет",
        ])


if __name__ == "__main__":
    unittest.main()

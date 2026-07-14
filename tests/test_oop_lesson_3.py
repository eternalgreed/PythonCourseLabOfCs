import unittest

from oop_lesson_3 import CityCar, DeliveryVan, ElectricEngine, GasolineEngine


class OopLessonThreeTest(unittest.TestCase):
    def test_gasoline_engine_uses_private_fuel_state(self):
        engine = GasolineEngine("G-100", 120, 10)

        self.assertFalse(hasattr(engine, "__fuel"))
        self.assertEqual(engine.get_fuel_level(), 10)

        engine.drive(30)

        self.assertEqual(engine.get_fuel_level(), 7)

    def test_electric_engine_uses_private_battery_state(self):
        engine = ElectricEngine("E-200", 90, 40)

        self.assertFalse(hasattr(engine, "__battery_charge"))
        self.assertEqual(engine.get_battery_charge(), 40)

        engine.charge(30)
        engine.drive(50)

        self.assertEqual(engine.get_battery_charge(), 60)

    def test_city_car_uses_engine_and_counts_mileage(self):
        engine = GasolineEngine("G-100", 120, 20)
        car = CityCar("Lada", "Vesta", engine, 41000, 480)

        damage = car.drive(25)

        self.assertEqual(damage, 120)
        self.assertEqual(car.get_mileage(), 41025)
        self.assertEqual(car.get_trunk_volume(), 480)
        self.assertTrue(car.fold_rear_seats())

    def test_delivery_van_tracks_cargo(self):
        engine = ElectricEngine("E-200", 90, 80)
        van = DeliveryVan("GAZ", "Sobol", engine, 120000, 900)

        self.assertTrue(van.load_cargo(350))
        self.assertFalse(van.load_cargo(700))
        self.assertEqual(van.get_cargo_weight(), 350)

        van.unload_cargo(120)

        self.assertEqual(van.get_cargo_weight(), 230)


if __name__ == "__main__":
    unittest.main()

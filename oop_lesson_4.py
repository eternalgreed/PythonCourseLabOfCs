import random


class Engine:
    def __init__(self, model, power):
        self.__model = model
        self.__power = power
        self.__is_running = False

    def start(self):
        self.__is_running = True

    def stop(self):
        self.__is_running = False

    def consume_energy(self, kilometers):
        return False

    def get_model(self):
        return self.__model

    def get_power(self):
        return self.__power

    def is_running(self):
        return self.__is_running


class GasolineEngine(Engine):
    def __init__(self, model, power, fuel):
        super().__init__(model, power)
        self.__fuel = fuel

    def refuel(self, liters):
        self.__fuel += liters

        if self.__fuel > 60:
            self.__fuel = 60

    def consume_energy(self, kilometers):
        fuel_needed = kilometers // 10

        if fuel_needed < 1:
            fuel_needed = 1

        if fuel_needed > self.__fuel:
            return False

        self.__fuel -= fuel_needed
        return True

    def get_fuel_level(self):
        return self.__fuel


class ElectricEngine(Engine):
    def __init__(self, model, power, battery_charge):
        super().__init__(model, power)
        self.__battery_charge = battery_charge

    def charge(self, percent):
        self.__battery_charge += percent

        if self.__battery_charge > 100:
            self.__battery_charge = 100

    def consume_energy(self, kilometers):
        charge_needed = kilometers // 5

        if charge_needed < 1:
            charge_needed = 1

        if charge_needed > self.__battery_charge:
            return False

        self.__battery_charge -= charge_needed
        return True

    def get_battery_charge(self):
        return self.__battery_charge


class Vehicle:
    def __init__(self, brand, model, engine):
        self.__brand = brand
        self.__model = model
        self.__engine = engine
        self.__mileage = 0

    def drive(self, kilometers):
        self.__engine.start()
        trip_completed = self.__engine.consume_energy(kilometers)
        self.__engine.stop()

        if trip_completed:
            self.__mileage += kilometers

        return trip_completed

    def get_full_name(self):
        return self.__brand + " " + self.__model

    def get_mileage(self):
        return self.__mileage

    def get_engine_model(self):
        return self.__engine.get_model()


class CityCar(Vehicle):
    def __init__(self, brand, model, engine, trunk_volume):
        super().__init__(brand, model, engine)
        self.__trunk_volume = trunk_volume
        self.__rear_seats_folded = False

    def open_trunk(self):
        return "Багажник открыт"

    def fold_rear_seats(self):
        self.__rear_seats_folded = True

    def get_trunk_volume(self):
        if self.__rear_seats_folded:
            return self.__trunk_volume + 300

        return self.__trunk_volume


class DeliveryVan(Vehicle):
    def __init__(self, brand, model, engine, max_cargo_weight):
        super().__init__(brand, model, engine)
        self.__max_cargo_weight = max_cargo_weight
        self.__cargo_weight = 0

    def load_cargo(self, weight):
        if self.__cargo_weight + weight > self.__max_cargo_weight:
            return False

        self.__cargo_weight += weight
        return True

    def unload_cargo(self, weight):
        self.__cargo_weight -= weight

        if self.__cargo_weight < 0:
            self.__cargo_weight = 0

    def get_cargo_weight(self):
        return self.__cargo_weight


class Animal:
    def foo(self):
        pass


class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")


class Bird(Animal):
    def foo(self):
        print("Птица поет")


def fill_animals(animals: list[Animal]) -> None:
    animals.clear()

    for _ in range(250):
        # Each call creates a new object instead of copying one reference.
        animals.append(Cat())
        animals.append(Bird())

    random.shuffle(animals)


def demonstrate_composition():
    gasoline_engine = GasolineEngine("G-100", 120, 20)
    electric_engine = ElectricEngine("E-200", 90, 80)

    city_car = CityCar("Lada", "Vesta", gasoline_engine, 480)
    delivery_van = DeliveryVan("GAZ", "Sobol", electric_engine, 900)

    print("Городской автомобиль:", city_car.get_full_name())
    print("Внутри него двигатель:", city_car.get_engine_model())
    print("Топливо до поездки:", gasoline_engine.get_fuel_level())
    city_car.drive(30)
    print("Пробег после поездки:", city_car.get_mileage())
    print("Топливо после поездки:", gasoline_engine.get_fuel_level())
    print()

    print("Фургон:", delivery_van.get_full_name())
    print("Внутри него двигатель:", delivery_van.get_engine_model())
    delivery_van.load_cargo(350)
    delivery_van.drive(50)
    print("Груз:", delivery_van.get_cargo_weight())
    print("Пробег после поездки:", delivery_van.get_mileage())
    print("Заряд после поездки:", electric_engine.get_battery_charge())


def main():
    print("4.1. Композиция")
    demonstrate_composition()

    print("\n4.3. Полиморфный вызов foo()")
    animals: list[Animal] = []
    fill_animals(animals)

    print("Всего объектов:", len(animals))

    for animal in animals:
        animal.foo()


if __name__ == "__main__":
    main()

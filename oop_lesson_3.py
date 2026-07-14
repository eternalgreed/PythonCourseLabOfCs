class Engine:
    def __init__(self, model, power):
        self.__model = model
        self.__power = power
        self.__is_running = False

    def start(self):
        self.__is_running = True

    def stop(self):
        self.__is_running = False

    def is_running(self):
        return self.__is_running

    def get_model(self):
        return self.__model

    def get_power(self):
        return self.__power


class GasolineEngine(Engine):
    def __init__(self, model, power, fuel):
        super().__init__(model, power)
        self.__fuel = fuel

    def refuel(self, liters):
        self.__fuel += liters

        if self.__fuel > 60:
            self.__fuel = 60

    def drive(self, kilometers):
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

    def drive(self, kilometers):
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
    def __init__(self, brand, model, engine, mileage):
        self.__brand = brand
        self.__model = model
        self.__engine = engine
        self.__mileage = mileage

    def drive(self, kilometers):
        self.__engine.start()
        can_drive = self.__engine.drive(kilometers)

        if can_drive:
            self.__mileage += kilometers

        self.__engine.stop()

        return self.__engine.get_power() if can_drive else 0

    def get_full_name(self):
        return self.__brand + " " + self.__model

    def get_mileage(self):
        return self.__mileage

    def get_engine_model(self):
        return self.__engine.get_model()


class CityCar(Vehicle):
    def __init__(self, brand, model, engine, mileage, trunk_volume):
        super().__init__(brand, model, engine, mileage)
        self.__trunk_volume = trunk_volume
        self.__rear_seats_folded = False

    def open_trunk(self):
        return "Trunk is open"

    def fold_rear_seats(self):
        self.__rear_seats_folded = True
        return self.__rear_seats_folded

    def get_trunk_volume(self):
        if self.__rear_seats_folded:
            return self.__trunk_volume + 300

        return self.__trunk_volume


class DeliveryVan(Vehicle):
    def __init__(self, brand, model, engine, mileage, max_cargo_weight):
        super().__init__(brand, model, engine, mileage)
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


def print_vehicle(vehicle):
    print("Vehicle:", vehicle.get_full_name())
    print("Engine:", vehicle.get_engine_model())
    print("Mileage:", vehicle.get_mileage())
    print()


def main():
    gasoline_engine = GasolineEngine("G-100", 120, 20)
    electric_engine = ElectricEngine("E-200", 90, 80)

    city_car = CityCar("Lada", "Vesta", gasoline_engine, 41000, 480)
    delivery_van = DeliveryVan("GAZ", "Sobol", electric_engine, 120000, 900)

    print("Initial objects")
    print_vehicle(city_car)
    print_vehicle(delivery_van)

    print("Gasoline engine fuel:", gasoline_engine.get_fuel_level())
    print("Electric engine charge:", electric_engine.get_battery_charge())
    print()

    city_car.drive(25)
    delivery_van.drive(50)

    print("After driving")
    print_vehicle(city_car)
    print_vehicle(delivery_van)
    print("Gasoline engine fuel:", gasoline_engine.get_fuel_level())
    print("Electric engine charge:", electric_engine.get_battery_charge())
    print()

    print("CityCar unique methods")
    print(city_car.open_trunk())
    print("Seats folded:", city_car.fold_rear_seats())
    print("Trunk volume:", city_car.get_trunk_volume())
    print()

    print("DeliveryVan unique methods")
    print("Load 350 kg:", delivery_van.load_cargo(350))
    print("Load 700 kg:", delivery_van.load_cargo(700))
    print("Current cargo:", delivery_van.get_cargo_weight())
    delivery_van.unload_cargo(120)
    print("Cargo after unloading:", delivery_van.get_cargo_weight())


if __name__ == "__main__":
    main()

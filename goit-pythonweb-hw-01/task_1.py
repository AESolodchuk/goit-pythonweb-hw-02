from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self) -> None:
        pass


class VehicleFactory(ABC):

    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class Car(Vehicle):
    def __init__(self, make, model, factory):
        self.make = make
        self.model = model
        self.factory = factory

    def start_engine(self):
        print(f"{self.make} {self.model} {self.factory}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model, factory):
        self.make = make
        self.model = model
        self.factory = factory

    def start_engine(self):
        print(f"{self.make} {self.model} {self.factory}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def __init__(self):
        self.name = "US Spec"

    def create_car(self, make, model):
        return Car(make, model, self.name)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.name)


class EUVehicleFactory(VehicleFactory):
    def __init__(self):
        self.name = "EU Spec"

    def create_car(self, make, model):
        return Car(make, model, self.name)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.name)


# Використання
def execute():
    us_spec = USVehicleFactory()
    eu_spec = EUVehicleFactory()

    ford = us_spec.create_car("Ford", "Mustang")
    reno = eu_spec.create_car("Reno", "Megan")

    harley_davidson = us_spec.create_motorcycle("Harley-Davidson", "Fat Bob")
    ducati = eu_spec.create_motorcycle("Ducati", "Streetfighter")

    ford.start_engine()
    reno.start_engine()

    harley_davidson.start_engine()
    ducati.start_engine()

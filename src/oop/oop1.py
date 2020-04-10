# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # Vehicle class
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print(f"{self.name}")


class FlightVehicle(Vehicle):  # FlightVehicle as a subclass of Vehicle
    def __init__(self, name):
        super().__init__(name)
        pass


class Starship(FlightVehicle):  # Starship as a subclass of FlightVehicle
    def __init__(self, name):
        super().__init__(name)
        pass


class Airplane(FlightVehicle):  # Airplane as a subclass of FlightVehicle
    def __init__(self, name):
        super().__init__(name)
        pass


class GroundVehicle(Vehicle):  # GroundVehicle as a subclass of Vehicle
    def __init__(self, name):
        super().__init__(name)
        pass


class Car(GroundVehicle):  # Car as a subclass of GroundVehicle
    def __init__(self, name):
        super().__init__(name)
        pass


class Motorcycle(GroundVehicle):  # Motorcycle as a subclass of GroundVehicle
    def __init__(self, name):
        super().__init__(name)
        pass

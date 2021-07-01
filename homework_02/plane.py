from homework_02 import exceptions
from homework_02.base import Vehicle


class Plane(Vehicle):

    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super.__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, plane):
        if self.cargo + plane <= self.max_cargo:
            self.cargo += plane
        else:
            raise exceptions.CargoOverload('Cargo Over load !!!')

    def remove_all_cargo(self):
        a = self.cargo
        self.cargo = 0
        return a

"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base, exceptions


class Plane(base.Vehicle):
    cargo = 0

    def __init__(self, max_cargo):
        self.max_cargo = max_cargo

    def load_cargo(self, num):
        if self.cargo + num <= self.max_cargo:
            self.cargo += num
        else:
            raise exceptions.CargoOverload('Cargo Over load !!!')

    def remove_all_cargo(self):
        yield self.cargo
        self.cargo = 0



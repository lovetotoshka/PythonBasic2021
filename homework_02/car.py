"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base, engine


class Car(base.Vehicle):
    engine = 0

    # def __init__(self, weight, fuel, fuel_consumption):
    #     super.__init__(weight, fuel, fuel_consumption)

    def set_engine(self, new_engine):
        self.engine = new_engine


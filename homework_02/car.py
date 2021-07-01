"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base


class Car(Vehicle):

    engine = 0

    def __init__(self, weight, fuel, fuel_consumption):
        super.__init__(weight, fuel, fuel_consumption)


    def set_engine(self):
        pass

#car = Car(101,101,11)
#print(car.weight, car.fuel, car.fuel_consumption)







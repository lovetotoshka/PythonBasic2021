from homework_02 import exceptions


class Vehicle:
    started = False

    def __init__(self, weight=100, fuel=100, fuel_consumption=10):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError('Low Fuel Error !!!')

    def move(self, distance):
        if self.fuel > 0 and 0 < self.fuel_consumption < self.fuel:
            max_distance = self.fuel // self.fuel_consumption
            if max_distance > distance:
                self.fuel = self.fuel - distance * self.fuel_consumption
            else:
                raise exceptions.NotEnoughFuel('Not Enough Fuel !!!')
        else:
            raise exceptions.NotEnoughFuel('Not Enough Fuel !!!')

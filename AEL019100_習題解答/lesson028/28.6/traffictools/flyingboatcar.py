from traffictools.airplane import *
from traffictools.car import *
from traffictools.boat import *

class FlyingBoatCar(Airplane, Car, Boat):
    def __init__(self):
        super().__init__()
        self._name = "FlyingBoatCar"
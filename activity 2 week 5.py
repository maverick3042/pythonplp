class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

def vehicle_action(vehicle):
    print(vehicle.move())

car = Car()
plane = Plane()

vehicle_action(car)
vehicle_action(plane)

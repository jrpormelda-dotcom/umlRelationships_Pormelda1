class Engine:
    def start(self):
        return "Vroom!"

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        return self.engine.start()

my_car = Car()
print(my_car.drive())
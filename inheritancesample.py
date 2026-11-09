class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")

    def make_sound(self):
        print("Some generic animal sound.")
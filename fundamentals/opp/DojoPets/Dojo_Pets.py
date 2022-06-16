from ninja import *
from pet import *

kai = Pet("Kai", "Doddle", ["high-five", "fetch", "roll over"], "woof!")
charlie = Ninja("Carlos", "Osornio", kai, ["salmon", "chicken", "beef"], "kibble")

charlie.walk().feed().bathe()
print(charlie.pet.name)

#SENSEI BONUS: Use Inheritance to create sub classes of pets.

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.sound = "Woof!"

class Cat(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.sound = "Meow!"
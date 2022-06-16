class Car: 
    def __init__(self, year, make, model, type, color, mileage=0, fuel=0):
        self.year = year
        self.make = make
        self.model = model
        self.type = type
        self.color = color
        self.mileage = mileage
        self.fuel = fuel

    def __repr__(self):
        return f"This car is a {self.color} {self.year} {self.make} {self.model} {self.type} with {self.mileage} miles and {self.fuel} gallons of fuel"

    def fill_tank(self, amount=100):
        if self.fuel == 100:
            print("Tank is full")
        elif self.fuel + amount > 100:
            self.fuel = 100
        else:
            self.fuel += amount
        return self

    def drive(self):
        if self.fuel > 10:
            self.fuel -= 10 
            self.mileage += 10
        else: 
            print(f"Sorry get some fuel!")
        return self

    def paint_job(self, color):
        self.color = color
        return self

car1 = Car(2016, "Toyota", "FR-S", "Standard", "silver")
car2 = Car(2016, "Mercedes", "GLA-250", "4-matic", "dark gray")

print(car1)
car1.paint_job("blue").fill_tank()
print(car1)

car1.drive().drive().drive().drive()
print(car1)
car1.fill_tank(20)
print(car1)


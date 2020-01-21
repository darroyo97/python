class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_info(self):
        print(self.make, self.model, self.year)


car1 = Car("toyota", "corolla", "2015")

car1.car_info()

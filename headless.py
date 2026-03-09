class BMW:
    
    def fuel_type(self):
        print("BMW fuel type: Petrol")
        
    def max_speed(self):
        print("BMW max speed: 250 km/h")


class Ferrari:
    
    def fuel_type(self):
        print("Ferrari fuel type: Petrol")
        
    def max_speed(self):
        print("Ferrari max speed: 340 km/h")


# objects
car1 = BMW()
car2 = Ferrari()

# polymorphism
for car in (car1, car2):
    car.fuel_type()
    car.max_speed()
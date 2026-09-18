from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles
car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "2CD567", 75)
motorbike = Motorbike("Honda", "Click", "3EF890", 125)

# Create a renter
renter = Renter("John", 12345)

print("=== Vehicles ===")
print(car)
print(electric_car)
print(motorbike)

print("\n=== Rent Vehicle ===")
car.rent()
print(car)

print("\n=== Return Vehicle ===")
car.return_vehicle()
print(car)

print("\n=== Renter ===")
print("Name:", renter.name)
print("License:", renter.license_no)
print("Rented vehicles:", renter.rented)

print("\n=== Error Handling ===")

# Bad name
try:
    bad_renter = Renter("", 12345)
except ValueError as e:
    print("Bad name:", e)

# Bad license
try:
    bad_renter = Renter("Alice", 0)
except ValueError as e:
    print("Bad license:", e)

# Changing to a bad name
try:
    renter.name = ""
except ValueError as e:
    print("Invalid name change:", e)

# Changing to a bad license
try:
    renter.license_no = -10
except ValueError as e:
    print("Invalid license change:", e)

print("\n=== Polymorphism ===")

vehicles = [
    Vehicle("Toyota", "Yaris", "1AB234"),
    ElectricCar("Tesla", "Model 3", "2CD567", 75),
    Motorbike("Honda", "Click", "3EF890", 125)
]

for vehicle in vehicles:
    print(vehicle)
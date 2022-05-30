number_of_flows = int(input())
tank_capacity = 255
total_liters = 0

for liters in range(number_of_flows):
    liters = int(input())

    if tank_capacity < liters:
        print("Insufficient capacity!")
        continue
    total_liters += liters
    tank_capacity -= liters

print(total_liters)

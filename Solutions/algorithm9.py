def calculate_rental_cost(days, miles):
    base_fee = 30
    cost_per_mile = 0.25

    total_cost = base_fee * days + cost_per_mile * miles
    return total_cost
  
print(calculate_rental_cost(5, 100))  # Output: 155.0 (base fee: 30*5 = 150, mileage cost: 0.25*100 = 25, total: 150+25 = 175.0)
print(calculate_rental_cost(3, 75))  # Output: 67.5 (base fee: 30*3 = 90, mileage cost: 0.25*75 = 18.75, total: 90+18.75 = 108.75)

import math

def unit_price(diameter, price):
    radius = diameter / 2 / 100
    area = math.pi * radius * radius
    return price / area

diameter1 = float(input("Enter diameter of first pizza (cm): "))
price1 = float(input("Enter price of first pizza (€): "))

diameter2 = float(input("Enter diameter of second pizza (cm): "))
price2 = float(input("Enter price of second pizza (€): "))

price_per_m2_1 = unit_price(diameter1, price1)
price_per_m2_2 = unit_price(diameter2, price2)

print(f"First pizza unit price: €{price_per_m2_1:.2f}/m²")
print(f"Second pizza unit price: €{price_per_m2_2:.2f}/m²")

if price_per_m2_1 < price_per_m2_2:
    print("First pizza is a better deal.")
elif price_per_m2_2 < price_per_m2_1:
    print("Second pizza is a better deal.")
else:
    print("Both pizzas have the same value.")

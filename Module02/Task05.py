LOTS_IN_POUND = 32
POUNDS_IN_TALENT = 20
GRAMS_IN_LOT = 13.3

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

total_lots = (talents * POUNDS_IN_TALENT * LOTS_IN_POUND) + (pounds * LOTS_IN_POUND) + lots
total_grams = total_lots * GRAMS_IN_LOT

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
e
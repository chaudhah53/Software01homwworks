numbers = []

while True:
    entry = input("Enter a number (empty to quit): ")
    if entry == "":
        break
    numbers.append(float(entry))

if numbers:
    print(f"Smallest number: {min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers were entered.")

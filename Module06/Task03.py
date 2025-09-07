def gallons_to_litres(gallons):
    return gallons * 3.78541

def main():
    while True:
        gallons = float(input("Enter quantity of gasoline in gallons (negative number to quit): "))
        if gallons < 0:
            print("Exiting program.")
            break
        litres = gallons_to_litres(gallons)
        print(f"{gallons} gallons = {litres:.2f} litres")

main()

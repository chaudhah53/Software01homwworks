airports = {}

while True:
    choice = input("\nChoose an option: (1) Enter new airport, (2) Fetch airport info, (3) Quit: ")

    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport added.")
    elif choice == "2":
        icao = input("Enter ICAO code: ").upper()
        if icao in airports:
            print(f"Airport name: {airports[icao]}")
        else:
            print("Airport not found.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

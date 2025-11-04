class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


def main():
    # Create a new car with registration number ABC-123 and maximum speed 142 km/h
    new_car = Car("ABC-123", 142)

    # Print out all properties of the new car
    print(f"Registration Number: {new_car.registration_number}")
    print(f"Maximum Speed: {new_car.max_speed} km/h")
    print(f"Current Speed: {new_car.current_speed} km/h")
    print(f"Travelled Distance: {new_car.travelled_distance} km")


# Call the main function
if __name__ == "__main__":
    main()
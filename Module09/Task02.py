class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed


def main():
    car = Car("ABC-123", 142)

    print("Initial state:")
    print(f"Registration Number: {car.registration_number}")
    print(f"Maximum Speed: {car.max_speed} km/h")
    print(f"Current Speed: {car.current_speed} km/h")
    print(f"Travelled Distance: {car.travelled_distance} km")
    print()

    print("Accelerating...")
    car.accelerate(30)
    print(f"After +30 km/h: {car.current_speed} km/h")
    car.accelerate(70)
    print(f"After +70 km/h: {car.current_speed} km/h")
    car.accelerate(50)
    print(f"After +50 km/h: {car.current_speed} km/h")
    print()

    print("Emergency brake applied!")
    car.accelerate(-200)
    print(f"Final speed: {car.current_speed} km/h")


if __name__ == "__main__":
    main()

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

    def drive(self, hours):
        distance_traveled = self.current_speed * hours
        self.travelled_distance += distance_traveled


def main():
    car = Car("ABC-123", 142)

    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)

    print(f"Before driving: {car.travelled_distance} km")
    print(f"Current speed: {car.current_speed} km/h")

    car.drive(1.5)

    print(f"After driving 1.5 hours: {car.travelled_distance} km")


if __name__ == "__main__":
    main()
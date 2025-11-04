import random


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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"\n{'Registration':<12} {'Max Speed':<12} {'Current Speed':<15} {'Distance':<12}")
        print("-" * 60)
        for car in self.cars:
            print(
                f"{car.registration_number:<12} {car.max_speed:<12} {car.current_speed:<15} {car.travelled_distance:<12}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


def main():
    cars = []
    for i in range(1, 11):
        registration = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(registration, max_speed))

    race = Race("Grand Demolition Derby", 8000, cars)

    print(f"Starting {race.name} - {race.distance} km race!")
    race.print_status()

    hour = 0
    while not race.race_finished():
        hour += 1
        race.hour_passes()

        if hour % 10 == 0:
            print(f"\n--- Status after {hour} hours ---")
            race.print_status()

    print(f"\n*** RACE FINISHED AFTER {hour} HOURS! ***")
    print("Final Results:")
    race.print_status()

    winner = max(race.cars, key=lambda car: car.travelled_distance)
    print(f"\nWinner: {winner.registration_number} with {winner.travelled_distance} km!")


if __name__ == "__main__":
    main()

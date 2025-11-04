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


def main():
    cars = []
    for i in range(1, 11):
        registration = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(registration, max_speed))

    hour = 0
    race_finished = False

    while not race_finished:
        hour += 1
        print(f"Hour {hour} of the race:")

        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

            if car.travelled_distance >= 10000:
                race_finished = True

        if hour % 10 == 0:
            print(f"Progress after {hour} hours:")
            for car in cars:
                print(f"{car.registration_number}: {car.travelled_distance} km")
            print()

    print("RACE FINISHED!")
    print(f"Race duration: {hour} hours")
    print()

    print("FINAL RESULTS:")
    print("-" * 60)
    print(f"{'Registration':<12} {'Max Speed':<10} {'Final Speed':<12} {'Distance':<12}")
    print("-" * 60)

    for car in cars:
        print(f"{car.registration_number:<12} {car.max_speed:<10} {car.current_speed:<12} {car.travelled_distance:<12}")


if __name__ == "__main__":
    main()
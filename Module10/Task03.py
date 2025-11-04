class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator moved up to floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator moved down to floor {self.current_floor}")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Floor {target_floor} is out of range ({self.bottom_floor}-{self.top_floor})")
            return

        print(f"Moving from floor {self.current_floor} to floor {target_floor}")

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()

        print(f"Arrived at floor {self.current_floor}")


class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_num, destination_floor):
        if elevator_num < 0 or elevator_num >= len(self.elevators):
            print(f"Elevator {elevator_num} does not exist")
            return

        print(f"Running elevator {elevator_num} to floor {destination_floor}")
        self.elevators[elevator_num].go_to_floor(destination_floor)

    def fire_alarm(self):
        print("FIRE ALARM! Moving all elevators to bottom floor!")
        for i, elevator in enumerate(self.elevators):
            print(f"Moving elevator {i} from floor {elevator.current_floor} to bottom floor")
            elevator.go_to_floor(self.bottom_floor)


def main():
    building = Building(1, 10, 3)

    building.run_elevator(0, 5)
    building.run_elevator(1, 8)
    building.run_elevator(2, 3)

    building.fire_alarm()


if __name__ == "__main__":
    main()

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


def main():
    elevator = Elevator(1, 10)

    elevator.go_to_floor(5)
    elevator.go_to_floor(1)


if __name__ == "__main__":
    main()

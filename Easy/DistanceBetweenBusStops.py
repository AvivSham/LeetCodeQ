from typing import List


def distance_between_bus_stops(distance: List[int], start: int, destination: int) -> int:
    clockwise = sum(distance[min(start, destination):max(start, destination)])
    counter_clockwise = sum(distance) - clockwise
    return min(clockwise, counter_clockwise)


if __name__ == '__main__':
    print(distance_between_bus_stops(distance=[1, 2, 3, 4], start=0, destination=1))
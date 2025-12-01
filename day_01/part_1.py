from typing import Iterable


def dial(position: int, direction: str, steps: int) -> tuple[int, int]:
    sign = 1 if direction == "R" else -1
    position = (position + sign * steps) % 100
    count = 0 if position != 0 else 1
    return position, count


def count_zero_landings(lines: Iterable[str]) -> int:
    dial_position = 50
    zero_landings = 0
    for line in lines:
        dir = line[0]
        steps = int(line[1:])
        dial_position, count = dial(dial_position, dir, steps)
        zero_landings += count
    return zero_landings


if __name__ == "__main__":
    with open("day_01/input.txt", "r") as file:
        print(count_zero_landings(file))

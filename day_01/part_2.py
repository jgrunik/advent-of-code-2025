from typing import Iterable


def dial(position: int, direction: str, steps: int) -> tuple[int, int]:
    sign = 1 if direction == "R" else -1
    # steps to first zero crossing
    first = (100 - sign * position) % 100 or 100
    # number of zero crossings
    crossings = 0 if steps < first else 1 + (steps - first) // 100
    # final dial position
    position = (position + sign * (steps % 100)) % 100
    return position, crossings


def count_zero_crossings(lines: Iterable[str]) -> int:
    dial_position = 50
    zero_crossings = 0

    for line in lines:
        dial_position, crossings = dial(
            dial_position,
            direction=line[0],
            steps=int(line[1:]),
        )
        zero_crossings += crossings

    return zero_crossings


if __name__ == "__main__":
    with open("day_01/input.txt", "r") as file:
        print(count_zero_crossings(file))

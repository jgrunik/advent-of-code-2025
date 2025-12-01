from day_01.part_2 import dial as dial_part_2, count_zero_crossings

with open("day_01/example.txt", "r") as file:
    example_instructions = file.read().strip().split("\n")


def test_example_part_2() -> None:
    assert count_zero_crossings(example_instructions) == 6


def test_crossings() -> None:
    assert dial_part_2(50, "R", 60) == (10, 1)
    assert dial_part_2(50, "L", 60) == (90, 1)
    assert dial_part_2(0, "R", 200) == (0, 2)
    assert dial_part_2(0, "L", 200) == (0, 2)
    assert dial_part_2(99, "R", 1) == (0, 1)
    assert dial_part_2(1, "L", 2) == (99, 1)


def test_no_crossings() -> None:
    assert dial_part_2(50, "R", 49) == (99, 0)
    assert dial_part_2(50, "L", 49) == (1, 0)
    assert dial_part_2(0, "R", 99) == (99, 0)
    assert dial_part_2(0, "L", 99) == (1, 0)


def test_multiple_crossings() -> None:
    assert dial_part_2(50, "R", 250) == (0, 3)
    assert dial_part_2(50, "L", 250) == (0, 3)
    assert dial_part_2(25, "R", 375) == (0, 4)
    assert dial_part_2(75, "L", 375) == (0, 4)


def test_count_crossings() -> None:
    instructions = ["R50", "R1", "L1", "L50", "R250", "L200"]
    assert count_zero_crossings(instructions) == 7

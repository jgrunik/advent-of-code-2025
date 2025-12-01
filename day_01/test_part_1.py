from day_01.part_1 import dial as dial_part_1, count_zero_landings

with open("day_01/example.txt", "r") as file:
    example_instructions = file.read().strip().split("\n")

# === PART 1 TESTS ===


def test_example_part_1() -> None:
    assert count_zero_landings(example_instructions) == 3


def test_landings() -> None:
    assert dial_part_1(50, "R", 60) == (10, 0)
    assert dial_part_1(50, "L", 60) == (90, 0)
    assert dial_part_1(0, "R", 200) == (0, 1)
    assert dial_part_1(0, "L", 200) == (0, 1)
    assert dial_part_1(99, "R", 1) == (0, 1)
    assert dial_part_1(1, "L", 2) == (99, 0)


def test_no_landings() -> None:
    assert dial_part_1(50, "R", 49) == (99, 0)
    assert dial_part_1(50, "L", 49) == (1, 0)
    assert dial_part_1(0, "R", 99) == (99, 0)
    assert dial_part_1(0, "L", 99) == (1, 0)


def test_multiple_landings() -> None:
    assert dial_part_1(50, "R", 250) == (0, 1)
    assert dial_part_1(50, "L", 250) == (0, 1)
    assert dial_part_1(25, "R", 375) == (0, 1)
    assert dial_part_1(75, "L", 375) == (0, 1)


def test_count_landings() -> None:
    instructions = ["R50", "R1", "L1", "L50", "R250", "L200"]
    assert count_zero_landings(instructions) == 4

"""Solution for day1 problem."""

import itertools
from typing import IO


def single_calibration(change_file: IO[str]) -> int:
    """Part 1."""
    frequency = 0
    for line in change_file:
        frequency += int(line)
    return frequency


def find_calibration(change_file: IO[str]) -> int:
    """Part 2."""
    frequency = 0
    seen = {0}
    for adjustment in itertools.cycle(change_file):
        frequency += int(adjustment)
        if frequency in seen:
            break
        seen.add(frequency)
    return frequency


if __name__ == "__main__":
    with open("inputs/day1.txt", "rt") as change_input:
        print(single_calibration(change_input))
        change_input.seek(0)
        print(find_calibration(change_input))

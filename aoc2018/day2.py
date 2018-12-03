"""Solution for day2 problem."""

from collections import Counter
import itertools
from typing import IO
from typing import Tuple


def check_string(instr: str) -> Tuple[bool, bool]:
    """Extract count check form a string."""
    count = Counter(instr)
    count_vals = count.values()
    return (2 in count_vals, 3 in count_vals)


def checksum(idfile: IO[str]) -> int:
    """Part 1."""
    double_count = 0
    triple_count = 0
    for checkstr in idfile:
        doubles, triples = check_string(checkstr)
        double_count += int(doubles)
        triple_count += int(triples)
    return double_count * triple_count


def match_common(idfile: IO[str]) -> str:
    """Part 2.

    Note:
        n**2 => sadness
    """
    for left, right in itertools.combinations(idfile, 2):
        common = "".join(lchar for lchar, rchar in zip(left, right) if lchar == rchar)
        if len(common) == len(left) - 1:
            return common
    return ""


if __name__ == "__main__":
    with open("inputs/day2.txt", "rt") as id_input:
        print(checksum(id_input))
        id_input.seek(0)
        print(match_common(id_input))

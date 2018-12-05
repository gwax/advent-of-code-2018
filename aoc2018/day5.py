"""Solution for day5 problem."""

import copy
import string
from typing import IO
from typing import List


def react_poly(polylist: List[str]) -> List[str]:
    """React the units and return a stripped list."""
    polylist = copy.copy(polylist)
    keep_going = True
    while keep_going:
        keep_going = False
        i = 0
        while i < len(polylist) - 1:
            if polylist[i] in string.ascii_lowercase:
                if polylist[i].upper() == polylist[i + 1]:
                    polylist[i : i + 2] = []
                    keep_going = True
                    continue
            elif polylist[i] in string.ascii_uppercase:
                if polylist[i].lower() == polylist[i + 1]:
                    polylist[i : i + 2] = []
                    keep_going = True
                    continue
            else:
                raise Exception(polylist[i])
            i += 1
    return polylist


def run(infile: IO[str]) -> None:
    """Solve the problems."""
    polylist = list(next(infile).strip())
    # Part 1
    reacted = react_poly(polylist)
    print(len(reacted))
    # Part 2
    variants = {}
    for character in string.ascii_lowercase:
        print(character)
        attempt = [c for c in reacted if c not in (character, character.upper())]
        variants[character] = react_poly(attempt)
    print(min(len(p) for p in variants.values()))


if __name__ == "__main__":
    with open("inputs/day5.txt", "rt") as input_file:
        run(input_file)

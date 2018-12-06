"""Solution for day6 problem."""

import collections
from typing import IO
from typing import Dict
from typing import Generator
from typing import Iterable
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple


def get_points(lines: Iterable[str]) -> Generator[Tuple[int, int], None, None]:
    """Convert input lines to (left, top) points."""
    for line in lines:
        if not line.strip():
            continue
        right, down = line.split(",")
        right = right.strip()
        down = down.strip()
        yield (int(right), int(down))


def nearest_grid(
    points: List[Tuple[int, int]]
) -> Dict[Tuple[int, int], Optional[Tuple[int, int]]]:
    """Check all in bound grid locations for nearest test point."""
    left = min(p[0] for p in points)
    right = max(p[0] for p in points)
    top = min(p[1] for p in points)
    bottom = max(p[1] for p in points)

    nearest_points = {}
    for i in range(left, right + 1):
        for j in range(top, bottom + 1):
            nearest: Set[Optional[Tuple[int, int]]] = set()
            best_distance = 1000000
            for point in points:
                distance = abs(i - point[0]) + abs(j - point[1])
                if distance < best_distance:
                    best_distance = distance
                    nearest = {point}
                elif distance == best_distance:
                    nearest.add(point)
            if len(nearest) == 1:
                [nearest_points[(i, j)]] = nearest
            else:
                nearest_points[(i, j)] = None
    return nearest_points


def distance_grid(points: List[Tuple[int, int]]) -> Dict[Tuple[int, int], int]:
    """Calculate total test point distance for all in bound grid locations."""
    left = min(p[0] for p in points)
    right = max(p[0] for p in points)
    top = min(p[1] for p in points)
    bottom = max(p[1] for p in points)

    grid = {}
    for i in range(left, right + 1):
        for j in range(top, bottom + 1):
            total_distance = 0
            for point in points:
                distance = abs(i - point[0]) + abs(j - point[1])
                total_distance += distance
            grid[(i, j)] = total_distance
    return grid


def run(infile: IO[str]) -> None:
    """Solve the problems"""
    points = list(get_points(infile))
    left = min(p[0] for p in points)
    right = max(p[0] for p in points)
    top = min(p[1] for p in points)
    bottom = max(p[1] for p in points)

    # Part 1
    grid_to_nearest = nearest_grid(points)
    excluded: Set[Optional[Tuple[int, int]]] = {None}
    for grid_point, nearest in grid_to_nearest.items():
        if grid_point[0] in (left, right) or grid_point[1] in (top, bottom):
            excluded.add(nearest)
    nearest_to_count = collections.Counter(
        [p for p in grid_to_nearest.values() if p not in excluded]
    )
    print(max(nearest_to_count.values()))

    # Part 2
    grid_to_distance = distance_grid(points)
    print(len([d for d in grid_to_distance.values() if d < 10000]))


if __name__ == "__main__":
    with open("inputs/day6.txt", "rt") as input_file:
        run(input_file)

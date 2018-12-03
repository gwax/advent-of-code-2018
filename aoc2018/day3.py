"""Solution for day3 problem."""

import collections
import re
from typing import IO
from typing import Dict
from typing import Iterable
from typing import NamedTuple
from typing import Set
from typing import Tuple

CLAIM_RE = re.compile(
    r"#(?P<id>\d+) @ "
    r"(?P<left>\d+),(?P<top>\d+): "
    r"(?P<width>\d+)x(?P<height>\d+)\n?"
)


class FabricClaim(NamedTuple):
    """Structure to store a fabric claim."""

    id: int
    left: int
    top: int
    width: int
    height: int


def parse_claim(claim: str) -> FabricClaim:
    """Parse a claim from a string."""
    match = CLAIM_RE.match(claim)
    if match is None:
        raise Exception(f"Cannot parse: {claim}")
    return FabricClaim(
        int(match.group("id")),
        int(match.group("left")),
        int(match.group("top")),
        int(match.group("width")),
        int(match.group("height")),
    )


def map_claims(claims: Iterable[FabricClaim]) -> Dict[Tuple[int, int], Set[int]]:
    """Place all claims on the fabric."""
    claim_map: Dict[Tuple[int, int], Set[int]] = collections.defaultdict(set)
    for claim in claims:
        for left in range(claim.left, claim.left + claim.width):
            for top in range(claim.top, claim.top + claim.height):
                claim_map[(left, top)].add(claim.id)
    return claim_map


def run(claimsfile: IO[str]) -> None:
    """Solve the problems."""
    # Part 1
    claims = [parse_claim(cstr) for cstr in claimsfile if cstr.strip()]
    counts = map_claims(claims)
    print(sum(1 for c in counts.values() if len(c) > 1))
    # Part 2
    seen: Set[int] = set()
    seen_overlapping: Set[int] = set()
    for claimed_square in counts.values():
        seen |= claimed_square
        if len(claimed_square) > 1:
            seen_overlapping |= claimed_square
    [seen_alone] = seen - seen_overlapping
    print(seen_alone)


if __name__ == "__main__":
    with open("inputs/day3.txt") as claims_input:
        run(claims_input)

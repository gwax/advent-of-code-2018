"""Tests for aoc2018.day3."""

import textwrap

import pytest

from aoc2018 import day3


@pytest.mark.parametrize(
    "claimstr, claim",
    [
        pytest.param("#123 @ 3,2: 5x4", day3.FabricClaim(123, 3, 2, 5, 4)),
        pytest.param("#123 @ 3,2: 5x4\n", day3.FabricClaim(123, 3, 2, 5, 4)),
    ],
)
def test_parse_claim(claimstr: str, claim: day3.FabricClaim) -> None:
    assert day3.parse_claim(claimstr) == claim


def test_map_claims() -> None:
    claimstrs = textwrap.dedent(
        """\
        #1 @ 1,3: 4x4
        #2 @ 3,1: 4x4
        #3 @ 5,5: 2x2
        """
    )
    claims = (day3.parse_claim(s) for s in claimstrs.split("\n") if s)
    counts = day3.map_claims(claims)
    assert counts == {
        (3, 1): {2},
        (4, 1): {2},
        (5, 1): {2},
        (6, 1): {2},
        (3, 2): {2},
        (4, 2): {2},
        (5, 2): {2},
        (6, 2): {2},
        (1, 3): {1},
        (2, 3): {1},
        (3, 3): {1, 2},
        (4, 3): {1, 2},
        (5, 3): {2},
        (6, 3): {2},
        (1, 4): {1},
        (2, 4): {1},
        (3, 4): {1, 2},
        (4, 4): {1, 2},
        (5, 4): {2},
        (6, 4): {2},
        (1, 5): {1},
        (2, 5): {1},
        (3, 5): {1},
        (4, 5): {1},
        (5, 5): {3},
        (6, 5): {3},
        (1, 6): {1},
        (2, 6): {1},
        (3, 6): {1},
        (4, 6): {1},
        (5, 6): {3},
        (6, 6): {3},
    }

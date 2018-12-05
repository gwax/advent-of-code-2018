"""Tests for aoc2018.day5."""

from typing import List

import pytest

from aoc2018 import day5


@pytest.mark.parametrize(
    "polyin, polyout", [pytest.param(list("dabAcCaCBAcCcaDA"), list("dabCBAcaDA"))]
)
def test_react_poly(polyin: List[str], polyout: List[str]) -> None:
    assert day5.react_poly(polyin) == polyout

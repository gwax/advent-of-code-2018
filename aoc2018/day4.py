"""Solution for day4 problem."""

import collections
import datetime as dt
import re
from typing import IO
from typing import Dict
from typing import Iterable
from typing import NamedTuple

GE_RE = re.compile(r"\[(?P<when>\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (?P<what>.*)")
SHIFT_RE = re.compile(r"Guard #(?P<id>\d+).*")


class GuardEvent(NamedTuple):
    """Event record."""

    when: dt.datetime
    what: str


def parse_guard_event(event: str) -> GuardEvent:
    """Parse a guard event string."""
    match = GE_RE.match(event)
    if match is None:
        raise Exception(f"Cannot parse: {event}")
    return GuardEvent(
        dt.datetime.strptime(match.group("when"), "%Y-%m-%d %H:%M"), match.group("what")
    )


def guard_sleep_minutes(
    guard_events: Iterable[GuardEvent]
) -> Dict[int, Dict[int, int]]:
    """Construct mapping {GuardId: {minute: times asleep}}"""
    sleep_minutes: Dict[int, Dict[int, int]] = collections.defaultdict(
        lambda: collections.defaultdict(int)
    )
    current_guard = -1
    fell_asleep = -1
    for guard_event in guard_events:
        match = SHIFT_RE.match(guard_event.what)
        if match:
            if fell_asleep >= 0:
                for i in range(fell_asleep, guard_event.when.minute):
                    print(current_guard, i)
                    sleep_minutes[current_guard][i] += 1
            current_guard = int(match.group("id"))
            fell_asleep = -1
        elif guard_event.what.startswith("wakes"):
            if fell_asleep >= 0:
                for i in range(fell_asleep, guard_event.when.minute):
                    sleep_minutes[current_guard][i] += 1
            fell_asleep = -1
        elif guard_event.what.startswith("falls"):
            fell_asleep = guard_event.when.minute
        else:
            raise Exception("WAT!")

    return sleep_minutes


def do_part_one(sleep_minutes: Dict[int, Dict[int, int]]) -> int:
    """Do part 1."""
    best_guard = -1
    best_minutes = -1
    best_time = -1
    for guard, minute_counts in sleep_minutes.items():
        total_minutes = sum(minute_counts.values())
        if total_minutes > best_minutes:
            best_guard = guard
            best_minutes = total_minutes
            best_count = -1
            for time, count in minute_counts.items():
                if count > best_count:
                    best_time = time
                    best_count = count
    return best_guard * best_time


def do_part_two(sleep_minutes: Dict[int, Dict[int, int]]) -> int:
    """Do part 2."""
    best_guard = -1
    best_minute = -1
    times_sleeping = -1
    for guard, minute_counts in sleep_minutes.items():
        for minute, counts in minute_counts.items():
            if counts > times_sleeping:
                times_sleeping = counts
                best_minute = minute
                best_guard = guard
    return best_guard * best_minute


def run(inputfile: IO[str]) -> None:
    """Solve the problems."""
    events = [parse_guard_event(e) for e in sorted(inputfile)]
    sleep_minutes = guard_sleep_minutes(events)
    # Part 1
    print(do_part_one(sleep_minutes))
    # Part 2
    print(do_part_two(sleep_minutes))


if __name__ == "__main__":
    with open("inputs/day4.txt", "rt") as infile:
        run(infile)

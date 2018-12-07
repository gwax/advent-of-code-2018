"""Solution for day7 problem."""

import re
from typing import IO
from typing import Dict
from typing import Generator
from typing import Iterable
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

STEP_RE = re.compile(
    r"Step (?P<before>[A-Z]) must be finished before step (?P<after>[A-Z]) can begin."
)


def get_directives(lines: Iterable[str]) -> Generator[Tuple[str, str], None, None]:
    """Get (before, after) directives from lines."""
    for line in lines:
        match = STEP_RE.match(line)
        if match is None:
            raise Exception("WAT!" + line)
        yield (match.group("before"), match.group("after"))


def prereqs(directives: Iterable[Tuple[str, str]]) -> Dict[str, Set[str]]:
    """Given a bunch of directives calculate nodes and prerequisites."""
    step_to_prereq: Dict[str, Set[str]] = {}
    for before, after in directives:
        step_to_prereq.setdefault(before, set())
        step_to_prereq.setdefault(after, set()).add(before)
    return step_to_prereq


def main(infile: IO[str]) -> None:
    """Solve the problems."""
    directives = get_directives(infile)
    step_to_prereq = prereqs(directives)
    # Part 1
    outstr = ""
    done: Set[str] = set()
    while True:
        ready = sorted(
            s for s, ps in step_to_prereq.items() if (not ps - done and s not in done)
        )
        if not ready:
            break
        outstr += ready[0]
        done.add(ready[0])
    print(outstr)
    # Part 2
    workers: List[Optional[Tuple[str, int]]] = [None] * 5
    time = 0
    done = set()
    queued: Set[str] = set()
    needed: Set[str] = set(step_to_prereq.keys())
    while needed - done:
        for i, worker in enumerate(workers):
            if worker is not None:
                character, done_at = worker
                if done_at <= time:
                    done.add(character)
                    workers[i] = None
        ready = sorted(
            s for s, ps in step_to_prereq.items() if (not ps - done and s not in queued)
        )
        for i, worker in enumerate(workers):
            if worker is None and ready:
                character, *ready = ready
                queued.add(character)
                done_at = time + 60 + ord(character) - ord("A") + 1
                workers[i] = (character, done_at)
        time += 1
    print(time - 1)


if __name__ == "__main__":
    with open("inputs/day7.txt", "rt") as input_file:
        main(input_file)

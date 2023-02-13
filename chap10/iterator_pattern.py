#%%
from typing import Iterable, Iterator


class CapitalIterable(Iterable[str]):
    def __init__(self, string: str) -> None:
        self.string = string
        
    def __iter__(self) -> Iterable[str]:
        return CapitalIterator(self.string)
        
        
class CapitalIterator(Iterator[str]):
    def __init__(self, string: str) -> None:
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0
        
    def __next__(self) -> str:
        if self.index == len(self.words):
            raise StopIteration()
        
        word = self.words[self.index]
        self.index += 1
        return word




iterable = CapitalIterable("the quick brown fox jumps over the lazy dog")


iterator = iter(iterable)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

# %% list comprehension
input_strings = ["1", "5", "28", "131", "3"]

output_integers = [int(num) for num in input_strings if len(num) < 3]



# %% set and dict comprehension
from typing import NamedTuple

class Book(NamedTuple):
    author: str
    title: str
    genre: str
    
    
book = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Jemisin", "The Broken Earth", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),
]

fantasy_authors = {b.author for b in book if b.genre == "fantasy"}
fantasy_authors


# %%
fantasy_title = {b.title: b for b in book if b.genre == "fantasy"}
fantasy_title




# %% generator

from pathlib import Path

full_log_path = Path.cwd() / "data" / "sample.log"
warning_log_path = Path.cwd() / "data" / "warnings.log"

with full_log_path.open() as source:
    warning_lines = (line for line in source if "WARN" in line)
    with warning_log_path.open("w") as target:
        for line in warning_lines:
            target.write(line) 




# %% generator function

import csv
import re
from pathlib import Path
from typing import Match,cast

def extract_and_parse_1(full_log_path: Path,
                        warning_log_path: Path
                        ) -> None:
    with warning_log_path.open("w") as target:
        writer = csv.writer(target, delimiter="\t")
        pattern = re.compile(
            r"(\w\w\w \d\d, \d\d\d\d \d\d:\d\d:\d\d) (\w+) (.*)")
        with full_log_path.open() as source:
            for line in source:
                if "WARN" in line:
                    line_groups = cast(
                        Match[str], pattern.match(line)).groups()
                    writer.writerow(line_groups)


# %% USING A GENERATOR 

from typing import Iterator, Iterable

def warnings_filter(soruce: Iterable[str]) -> Iterator[tuple[str, ...]]:
    pattern = re.compile(
            r"(\w\w\w \d\d, \d\d\d\d \d\d:\d\d:\d\d) (\w+) (.*)"
        )
    for line in source:
        if "WARN" in line:
            yield tuple(
                cast(type=Match[str], value=pattern.match(line)).groups()
            )


def extract_and_parse_3(
    full_log_path: Path, warning_log_path: Path
) -> None:
    with warning_log_path.open(mode="w") as target:
        writer = csv.writer(target, delimiter="\t")
        with full_log_path.open() as infile:
            filter = warnings_filter(infile)
            for line_groups in filter:
                writer.writerow(line_groups)
            



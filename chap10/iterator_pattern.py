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

output_integers = [int(num) for num in input_strings]



# %%

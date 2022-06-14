#%%

from typing import List
class EvenOnly(List[int]):
    def append(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Only integers can be added")
        if value % 2 != 0:
            raise ValueError("Only even numbers can be added")
        super().append(value)
# %%
e = EvenOnly()
e.append("a string")
# %%
e.append(3)
# %%
e.append(2)

# %%
from typing import Union

#%%
def funny_division(divisor: float) -> Union[str, float]:
    try:
        if divisor == 13:
            raise ValueError("13 is an unlucky")
        return 100 / divisor
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"

#%%
print(funny_division(0))
print(funny_division(50.0))

funny_division("hello world")

# %%
for val in (0, 'hello', 50.0, 13):
    print(f"Testing {val!r}:", end=" ")
    print(funny_division(val))

#%%
try:
    raise ValueError("This is an argument")
except ValueError as e:
    print(f"The exception arguments were {e.args}")



# %%

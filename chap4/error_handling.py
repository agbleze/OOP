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

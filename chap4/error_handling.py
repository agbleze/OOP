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

#%%
some_exceptions = [ValueError, TypeError, IndexError, None]

for choice in some_exceptions:
    try:
        print(f"\nRaising {choice}")
        if choice:
            raise choice("An error")
        else:
            print("no exception raised")
    except ValueError:
        print("Caught a ValueError")
    except TypeError:
        print("Caught a TypeError")
    except Exception as e:
        print(f"Caught some other error: {e.__class__.__name__}")
    else:
        print("This code called if there is no exception")
    finally:
        print("This cleanup code is always called")




# %% defining own exception
from decimal import Decimal
class InvalidWithdrawal(ValueError):
    def __init__(self, balance: Decimal, amount: Decimal)->None:
        super().__init__(f"account doesnt have ${amount}")
        self.amount = amount
        self.balance = balance
        
    def overage(self) -> Decimal:
        return self.amount - self.balance

# %%
try:
    balance = Decimal('25.00')
    raise InvalidWithdrawal(balance, Decimal('50.00'))
except InvalidWithdrawal as ex:
    print("I'm sorry, but your withdrawal is "
          "more than your balance by "
          f"${ex.overage()}")

# %%
row = {"sepal_length": "5.1", "sepal_width": "3.5",
       "petal_length": "1.4", "petal_width": "0.2",
       "sepcies": "Iris-setosa"}
# %%
@classmethod
def from_dict(cls, row: dict[str, str]) -> "KnownSample":
    if row["species"] not in {
        "Iris-setosa", "Iris-versicolour", "Iris-virginica"}:
        raise InvalidSampleError(f"invalid species in {row!r}")
    try:
        return cls(
            species=row["species"],
            sepal_length=float(row["sepal_length"]),
            sepal_width=float(row["sepal_width"]),
            petal_length=float(row["petal_length"]),
            petal_width=float(row["petal_width"]),
        )
    except ValueError as ex:
        raise InvalidSampleError(f"invalid {row!r}")
    
    
class TrainingKnownSample(KnownSample):
    @classmethod
    def from_dict(cls, row: dict[str, str]) ->  "TrainingKnownSample":
        return cast(TrainingKnownSample, super().from_dict(row))   
    
    
    
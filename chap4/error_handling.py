#%%

from typing import List, Optional
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
    
#%%
class Sample:
    def __init__(self, sepal_length: float, 
                 sepal_width: float,
                 petal_length: float, 
                 petal_width: float,
                 species: Optional[str]= None
                 )-> None:
        self.sepal_length = sepal_length,
        self.sepal_width = sepal_width,
        self.petal_length = petal_length,
        self.petal_width = petal_width,
        self.species = species,
        self.classification: Optional[str] = None
        
        
    def __repr__(self)->str:
        if self.species is None:
            known_unknown = "UnknownSample"
        else:
            known_unknown = "KnownSample"
            
        if self.classification is None:
            classification = ""
        else:
            classification = f", {self.classification}"
        
        return (
            f"{known_unknown}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length} "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}"
            f"{classification}"
            f")"
        )
        
    def classify(self, classification: str) -> None:
        self.classification = classification
        
    def matches(self) -> bool:
        return self.species == self.classification
        
class KnownSample(Sample):
    def __init__(self,
                 species: str,
                 sepal_length: float, 
                 sepal_width: float,
                 petal_length: float, 
                 petal_width: float,
                 ) -> None:
        super().__init__(
            sepal_length = sepal_length,
            sepal_width = sepal_width,
            petal_length = petal_length,
            petal_width = petal_width,
        )
        self.species = species
        
    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length={self.sepal_length}, "
            f"sepal_width={self.sepal_width}, "
            f"petal_length={self.petal_length}, "
            f"petal_width={self.petal_width}, "
            f"species={self.species!r}"
            f")"
        )
class TrainingKnownSample(KnownSample):
    @classmethod
    def from_dict(cls, row: dict[str, str]) ->  "TrainingKnownSample":
        return cast(TrainingKnownSample, super().from_dict(row))   
    
# %%
valid = {"sepal_length": "5.1", "sepal_width": "3.5", 
         "petal_length": "1.4", "petal_width": "0.2",
         "species": "Iris-setosa"}






# %%

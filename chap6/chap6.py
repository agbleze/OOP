#%%
from __future__ import annotations
import abc
from typing import Iterable, Iterator, Sequence, Mapping
from typing import Protocol, Any, overload, Union
import bisect
from collections.abc import (Container, Sized, Set)
class MediaLoader(abc.ABC):
    @abc.abstractmethod
    def play(self) -> None:
        ...
        
    @property
    @abc.abstractmethod
    def ext(self) -> str:
        ...

# %%
class Wav(MediaLoader):
    pass
# %%
x = Wav()
# %%
class Ogg(MediaLoader):
    ext = '.ogg'
    def play(self):
        pass
o = Ogg()

# %%

Container.__abstractmethods__
# %%
class OddIntegers:
    def __contains__(self, x: int) -> bool:
        return x %2 != 0
odd = OddIntegers()
isinstance(odd, Container)
# %%
issubclass(OddIntegers, Container)
# %%
1 in odd
# %%
BaseMapping = abc.Mapping[Comparable, Any]
class Lookup(BaseMapping):
    @overload
    def __init__(
        self, 
        source: Iterable[tuple[Comparable, Any]]
    ) -> None:
        ...
        
    @overload
    def __init__(self, source: BaseMapping) -> None:
        ...
    def __init__(
        self,
        source: Union[Iterable[tuple[Comparable, Any]]
                      BaseMapping,
                      None] = None,
    ) -> None:
        sorted_pairs: Sequence[tuple[Comparable, Any]]
        if isinstance(source, Sequence):
            sorted_pairs = sorted(source)
        elif isinstance(source, abc.Mapping):
            sorted_pairs = sorted(source.items())
        else:
            sorted_pairs = []
        self.key_list = [p[0] for p in sorted_pairs]
        self.value_list = [p[1] for p in sorted_pairs]
    
    def __len__(self) -> int:
        return len(self.key_list)
    
    def __iter__(self) -> Iterator[Comparable]:
        return iter(self.key_list)
    
    def __contains__(self, key: object) -> bool:
        index = bisect.bisect_left(self.key_list, key)
        return key == self.key_list[index]
    
    def __getitem__(self, key: Comparable) -> Any:
        index = bisect.bisect_left(self.key_list, key)
        if key == self.key_list[index]:
            return self.value_list[index]
        raise KeyError(key)
        
class Comparable(Protocol):
    
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...      
        
        
                
# %%
import abc
import random
class Die(abc.ABC):
    def __init__(self) -> None:
        self.face: int
        self.roll()
        
    @abc.abstractmethod
    def roll(self) -> None:
      ...
    
    def __repr__(self) -> str:
        return f"{self.face}"
#%%
class D4(Die):
    def roll(self) -> None:
        self.face = random.choice((1,2,3,4))
        
class D6(Die):
    def roll(self) -> None:
        self.face = random.randint(1,6)
        
#%%
from typing import Type, Set
class Dice(abc.ABC):
    def __init__(self, n: int, die_class: Type[Die]) -> None:
        self.dice = [die_class() for _ in range(n)]
        
    @abc.abstractmethod
    def roll(self) -> None:
        ...
    
    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice)

class SimpleDice(Dice):
    def roll(self) -> None:
        for d in self.dice:
            d.roll()


#%%
sd = SimpleDice(6, D6)
sd.roll()
sd.total

#%%
from typing import Iterable
class YachtDice(Dice):
    def __init__(self) -> None:
        super().__init__(5, D6)
        self.saved: Set[int] = set()
        
    def saving(self, positions: Iterable[int]) -> "YachtDice":
        if not all(0 <= n < 6 for n in positions):
            raise ValueError("Invalid position")
        self.saved = set(positions)
        return self
    def roll(self) -> None:
        for n, d in enumerate(self.dice):
            if n not in self.saved:
                d.roll()
        self.saved = set()
        

#%%
sd = YachtDice()
sd.roll()
sd.dice
sd.saving([0,1,2]).roll()
sd.dice

#%%
Die.__abstractmethods__
Die.roll.__isabstractmethod__

#%%
# extending metaclass
class DieM(metaclass = abc.ABCMeta):
    def __init__(self) -> None:
        self.face: int
        self.roll()
    @abc.abstractmethod
    def roll(self) -> None:
        ...

#%% Operator overloading
# deals with expanding operators to work with other data types
from pathlib import Path
home = Path.home()
home / "minconda3" / "envs"
# the / operator is used to connect a Path object to
# a string object to create new Path object

#%%
class DDice:
    def __init__(self, *die_class: Type[Die]) -> None:
        self.dice = [dc() for dc in die_class]
        self.adjust: int = 0
    
    def plus(self, adjust: int = 0) -> "DDice":
        self.adjust = adjust
        return self
    
    def roll(self) -> None:
        for d in self.dice:
            d.roll()
            
    @property
    def total(self) -> int:
        return sum(d.face for d in self.dice) + self.adjust
    
    def __add__(self, die_class: Any) -> "DDice":
        if isinstance(die_class, type) and issubclass(die_class, Die):
            new_classes = [type(d) for d in self.dice] + [die_class]
            new = DDice(*new_classes).plus(self.adjust)
            return new
        elif isinstance(die_class, int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
            return new
        else:
            return NotImplemented
        
    def __radd__(self, die_class: Any) -> "DDice":
        if isinstance(die_class, type) and issubclass(die_class, Die):
            new_classes = [die_class] + [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(self.adjust)
            return new
        elif isinstance(die_class, int):
            new_classes = [type(d) for d in self.dice]
            new = DDice(*new_classes).plus(die_class)
            return new
        else:
            return NotImplemented
        
    def __mul__(self, n: Any) -> "DDice":
        if isinstance(n, int):
            new_classes = [type(d) for d in self.dice for _ in range(n)]
            return DDice(*new_classes).plus(self.adjust)
        else:
            NotImplemented
            
    def __rmul__(self, n: Any) -> "DDice":
        if isinstance(n, int):
            new_classes = [type(d) for d in self.dice for _ in range(n)]
            return DDice(*new_classes).plus(self.adjust)
        else:
            return NotImplemented
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
    





# %%

#%%
from __future__ import annotations
import abc
from typing import Iterable, Iterator, Sequence, Mapping
from typing import Protocol, Any, overload, Union
import bisect

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
from collections.abc import Container
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
        
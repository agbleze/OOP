#%%
from __future__ import annotations
from math import hypot
from typing import Tuple, List, Optional, Iterable, Union

Point = Tuple[float, float]

def distance(p_1: Point, p_2: Point) -> float:
    return hypot(p_1[0] - p_2[0], p_1[1] - p_2[1])

Polygon = List[Point]

def perimeter(polygon: Polygon) -> float:
    pairs = zip(polygon, polygon[1:] + polygon[:1])
    return sum(distance(p1, p2) for p1, p2 in pairs)


#################################################
class Point:
    def __init__(self, x: float, y:float) -> None:
        self.x = x
        self.y = y
        
    def distance(self, other: 'Point') -> float:
        return hypot(self.x -other.x, self.y - other.y)

class Polygon:
    def __init__(self) -> None:
        self.vertices: List[Point] = []
        
    def add_point(self, point: Point) -> None:
        self.vertices: List[Point] = []
        
    def perimeter(self) -> float:
        pairs = zip(self.vertices, self.vertices[1:] + self.vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)


# %%
square = Polygon()
square.add_point(Point(1,1))
square.add_point(Point(1,2))
square.add_point(Point(2,2))
square.add_point(Point(2,1))
square.perimeter()




# %%
square = [(1,1), (1,2), (2,2), (2,1)]
perimeter(square)
# %%
class Polygon_2:
    def __init__(self, vertices: Optional[Iterable[Point]] = None)-> None:
        self.vertices = list(vertices) if vertices else []
        
    def perimeter(self) -> float:
        pairs = zip(self.vertices, self.vertices[1:] + self.vertices[:1])
        return sum(p1.distance(p2) for p1, p2 in pairs)
    
square = Polygon_2([Point(1,1), Point(2,2), Point(2,1)])        
square.perimeter()        
    
# %%
Pair = Tuple[float, float]
Point_or_Tuple = Union[Point, Pair]

class Polygon_3:
    def __init__(self, vertices: Optional[Iterable[Point_or_Tuple]] = None) -> None:
        self.vertices: List[Point] = []
        if vertices:
            for point_or_tuple in vertices:
                self.vertices.append(self.make_point(point_or_tuple))
    @staticmethod
    def make_point(item: Point_or_Tuple) -> Point:
        return item if isinstance(item, Point) else Point(*item)
                

#%% problematic approach suggest by others -- Not encourange
class Color:
    def __init__(self, rgb_value: int, name: str) -> None:
        self._rgb_value = rgb_value
        self._name = name
        
    def set_name(self, name: str) -> None:
        self._name = name
        
    def get_name(self) -> str:
        return self._name
    def set_rgb_value(self, rgb_value: int) -> None:
        self._rgb_value = rgb_value
        
    def get_rgb_value(self) -> int:
        return self._rgb_value
    
#%%
c = Color(0xff0000, "bright red")
c.get_name()    
c.set_name("red")
c.get_name()    
    
#%% expanding the above class
class Color_V:
    def __init__(self,rgb_value: int, name: str) -> None:
        self._rgb_value = rgb_value
        if not name:
            raise ValueError(f"Invalid name {name!r}")
        self._name = name
        
        def set_name(self, name: str) -> None:
            if not name:
                raise ValueError(f"Invalid name {name!r}")
            self._name = name
            
class Color_VP:
    def __init__(self, rgb_value: int, name: str) -> None:
        self._rgb_value = rgb_value
        if not name: 
            raise ValueError(f"Invalid name {name!r}")            
        self._name = name
        
    def _set_name(self, name: str) -> None:
        if not name:
            raise ValueError(f"Invalid name {name!r}")    
        self._name = name
        
    def _get_name(self) -> str:
        return self._name
    
    name = property(_get_name, _set_name)    
# %%
c = Color_VP(0xff0000, "bright red")
c.name

c.name = "red"
c.name

#c.name = ''

#%% docstring in property
class NorwegianBlue:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str
    
    def _get_state(self) -> str:
        print(f"Getting {self._name}'s State")
        return self._state
    
    def _set_state(self, state: str) -> None:
        print(f"Setting {self._name}'s State to {state!r}")
        self._state = state
        
    def _del_state(self) -> None:
        print(f"{self._name} is pushing up daisies!")
        del self._state
        
    silly = property(_get_state, _set_state, _del_state,
                     "This is a silly property")
    
    
p = NorwegianBlue("Polly")
p.silly = "Pinning for the fjords"
p.silly    
    
del p.silly    
    
#%%
class NorwegianBlue_P:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str
    
    @property
    def silly(self) -> str:
        print(f"Getting {self._name}'s State")
        return self._state   
    
    @silly.setter
    def silly(self, state: str) -> None:
        print(f"Setting {self._name}'s State to {state!r}")
        self._state = state 
        
    @silly.deleter
    def silly(self) -> None:
        print(f"{self._name} is pushing up daisies!")
        del self._state
    
    
#%% caching with getter
from urllib.request import urlopen
from typing import Optional, cast

class WebPage:
    def __init__(self, url: str) -> None:
        self.url = url
        self._content: Optional[bytes] = None
        
    @property
    def content(self) -> bytes:
        if self._content is None:
            print("Retrieving New Page...")
            with urlopen(self.url) as response:
                self._content = response.read()
        return self._content

#%%
import time

#%%
webpage = WebPage("http://ccphillips.net/") 

now = time.perf_counter()
content1 = webpage.content
first_fetch = time.perf_counter() - now

#%%
now = time.perf_counter()
content2 = webpage.content
second_fetch = time.perf_counter() - now
   
assert content2 == content1, "Problem: Pages were different"
print(f"Initial Request {first_fetch: .5f}")
print(f"Subsequent Request {second_fetch: .5f}")
    
#%%
from typing import List

class AverageList(List[int]):
    @property
    def average(self) -> float:
        return sum(self) / len(self)

#%%    
a = AverageList([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
a.average   

#%% Manage objects
from __future__ import annotations
import fnmatch
from pathlib import Path
import re
import zipfile
from abc import ABC, abstractmethod

class ZipProcessor(ABC):
    def __init__(
        self,
        archive: Path
    ) -> None:
        self.archive_path = archive,
        self._pattern: str
        
    def process_files(self, pattern: str) -> None:
        self._pattern = pattern
        input_path, output_path = self.make_backup()
        
        with zipfile.ZipFile(output_path, "w") as output:
            with zipfile.ZipFile(input_path) as input:
                self.copy_and_transform(input, output)
                
    def make_backup(self) -> tuple[Path, Path]:
        input_path = self.archive_path.with_suffix(
            f"{self.archive_path.suffix}.old"
        )
        output_path = self.archive_path
        self.archive_path.rename(input_path)
        return input_path, output_path
    
    def copy_and_transform(
        self, input: zipfile.ZipFile, output: zipfile.ZipFile
    ) -> None:
        for item in input.infolist():
            extracted = Path(input.extract(item))
            if self.matches(item):
                print(f"Transform {item}")
                self.transform(extracted)
            else:
                print(f"Ignore {item}")
            output.write(extracted, item.filename)
            self.remove_under_cwd(extracted)
            
    def matches(self, item: zipfile.ZipInfo) -> bool:
        return(not item.is_dir() and fnmatch(item.filename, self._pattern))
    
    def remove_under_cwd(self, extracted: Path) -> None:
        extracted.unlink()
        for parent in extracted.parents:
                    if parent == Path.cwd():
                        break
                    parent.rmdir()
    
    @abstractmethod
    def transform(self, extracted: Path) -> None:
        ...
class TextTweaker(ZipProcessor):
    def __init__(self, archive: Path) -> None:
        super().__init__(archive)
        self.find: str
        self.replace: str
    
    def find_and_replace(self, find: str, replace: str) -> "TextTweak":
        self.find = find
        self.replace = replace
        return self 
    
    def transform(self, extracted: Path) -> None: 
        input_text = extracted.read_text()
        output_text = re.sub(self.find, self.replace, input_text)
        extracted.write_text(output_text) 
        
#%%
from PIL import Image
class ImgTweaker(ZipProcessor):
    def transform(self, extracted: Path) -> None:
        image = Image.open(extracted)
        scaled = image.resize(size=(640, 960))
        scaled.save(extracted)
 

#%% # case study     
class SampleReader:
    """See iris.names for attribute ordering in bezdekIris.data file
    """
    target_class = Sample
    header = [
        "sepal_length", "sepal_width",
        "petal_length", "petal_width", "class"
    ]
    
    def __init__(self, source:Path) -> None:
        self.source = source
        
    def sample_iter(self) -> Iterator[Sample]:
        target_class = self.target_class
        with self.source.open() as source_file:
            reader = csv.DictReader(source_file, self.header)
            for row in reader:
                try:
                    sample = target_class(
                        sepal_length=float(row["sepal_length"]),
                        sepal_width=float(row["sepal_width"]),
                        petal_length=float(row["petal_length"]),
                        petal_width=float(row["petal_width"])
                    )
                except ValueError as ex:
                    raise BadSampleRow(f"Invalid {row!r}") from ex
                yield sample

class BadSampleRow(ValueError):
    pass

class Purpose(enum.IntEnum):
    Classification = 0
    Testing = 1
    Training = 2
                
class KnownSample(Sample):
    def __init__(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        purpose: int,
        species: str,
    ) -> None:
        purpose_enum = Purpose(purpose)
        if purpose_enum not in {Purpose.Training, Purpose.Testing}:
            raise ValueError(
                f"Invalid purpose: {purpose!r}: {purpose_enum}"
            ) 
        super().__init__(
            sepal_length = sepal_length,
            sepal_width = sepal_width,
            petal_length = petal_length,
            petal_width = petal_width
        )   
        self.purpose = purpose_enum
        self.species = species
        self._classification: Optional[str] = None
    def matches(self) -> bool:
        return self.species == self.classification            
    @property
    def classification(self) -> Optional[str]:
        if self.purpose == Purpose.Testing:
            return self._classification
        else:
            raise AttributeError(f"Training samples have no classification")



           
# if __name__ == "__main__":
#     sample_zip = Path("sample.zip")
#     zr = ZipReplace(sample_zip, "*.md", "xyzzy", "plover's egg")
#     zr.find_and_replace()
                







# %%

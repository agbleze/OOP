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

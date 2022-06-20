#%%
from __future__ import annotations
from math import hypot
from typing import Tuple, List, Optional, Iterable

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

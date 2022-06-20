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



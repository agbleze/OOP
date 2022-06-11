class Point:
    """
    Represents a point in two dimensional geometric coordinates.
    """
    def __init__(self, 
                 x: float = 0, 
                 y: float = 0
    )-> None:
        pass

def main()-> None:
    """
    Does the useful work.
    
    >>> main()
    p1.calculate_distance(p2)=5.0
    """
    p1 = Point()
    p2 = Point(3, 4)
    print(f"{p1.calculate_distance(p2)=}")
    
if __name__ == '__main__':
    main()
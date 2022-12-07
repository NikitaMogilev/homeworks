from math import hypot
from itertools import combinations


def distance(p1, p2):
    """Euclidean distance between two points."""
    x1, y1 = p1
    x2, y2 = p2
    return hypot(x2 - x1, y2 - y1)


list_of_points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (65, 52)]

result = sum([distance(*combo) for combo in combinations(list_of_points, 2)])
print(result)

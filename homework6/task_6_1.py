from math import hypot


def distance(*args):
    sum_of_distance = 0
    for index, points in enumerate(args):
        if index == len(args)-1:
            break
        x1, y1 = points
        x2, y2 = args[index+1]
        lengh = hypot(x2 - x1, y2 - y1)
        sum_of_distance += lengh
    return sum_of_distance


result = round(distance((1, 1), (1, 2), (2, 2), (3, 3)), 2)
print(result)

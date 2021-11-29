import math
import functools

def distanceBetweenPoints(point1, point2):
    x, y = point1
    x1, y1 = point2
    return math.sqrt(math.pow(x1 - x, 2) + math.pow(y1 - y, 2))

def standardDeviation(values):
    size = len(values)
    average = sum(values)/size
    topAux = sum(map(lambda value: pow(value - average, 2), values))
    return math.sqrt(topAux/(size-1))
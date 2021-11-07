import math

def distanceBetweenPoints(point1, point2):
    x, y = point1
    x1, y1 = point2
    return math.sqrt(math.pow(x1 - x, 2) + math.pow(y1 - y, 2))
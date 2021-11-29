import math

def distanceBetween(person1, person2):
    return math.sqrt( (person1.x - person2.x)**2 + (person1.y-person2.y)**2)
import math

def distanceBetween(person1, person2):
    return math.sqrt( (person1.x - person2.x)**2 + (person1.y-person2.y)**2)

def angleBetween(person1, person2):
    if person2 == "exit":
        difx = 20 - person1.x
        if person1.y < 8.5:
            dify = 8.5 - person1.y
        elif person1.y > 11.5:
            dify = 11.5 - person1.y
        else:
            dify = 0
        angle = math.atan(dify / difx)

    else:
        difx = abs(person1.x - person2.x)
        dify = abs(person1.y - person2.y)
        if difx == 0:
            difx = 0.0000001
        angle = math.atan(dify/difx)
        if person1.x < person2.x:
            if person1.y < person2.y:
                angle += 0
            else:
                angle = (2*math.pi) - angle
                #angle += (math.pi * 3) / 2
        else:
            if person1.y < person2.y:
                angle = math.pi - angle
                #angle += math.pi / 2
            else:
                angle += math.pi
    return angle

def totalSpeed(person):
    return math.sqrt(person.vx**2 + person.vy**2)


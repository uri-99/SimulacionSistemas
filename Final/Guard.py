#Tau y KillProbability variable como variación de su training (caso 3).
#Se varía su cantidad en el caso 2. Caso 5 doble corona
#caso 4 matan de lejos

class Guard:
    def __init__(self, x, y, size, mass):
        self.x = x
        self.y = y
        self.size = size
        self.mass = mass
        isDead = False

    def move(self, dt, VIP, attackers):
        for person in attackers:
            dist = distanceBetween(self, person)
            difx = self.x - person.x
            dify = self.y - person.y
            #if dist <= (self.size/2) + (person.size/2):
                #battle, hasta que puede quedar mejor en attacker.py

        #posición respectiva al vip nada mas, él tiene el social force
        return

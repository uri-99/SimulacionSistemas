#stats fijos siempre
import random

class VIP:

    VIPspeed = 1

    def __init__(self, x, y, size, mass):
        self.x = x
        self.y = y
        self.size = size
        self.mass = mass
        self.isDead = False
        self.hasEscaped = False
        self.dieChance = 0.5

    def move(self, dt):
        if self.x >= 20:
            self.hasEscaped = True

        granular = [0, 0]
        social = [0, 0]
        drive = [0, 0]

        for person in attackers:
            dist = distanceBetween(self, person)
            difx = self.x - person.x
            dify = self.y - person.y
            if dist <= (self.size/2) + (person.size/2):#un atacker toca al vip
                self.isDead = self.hasDied()

            angle = math.atan(dify / difx)
            social[0] += ( self.A ** (dist/self.B) ) * math.cos(-angle)
            social[1] += ( self.A ** (dist/self.B) ) * math.sin(-angle)

            targetX = VIP.x
            targetY = VIP.y
            drive[0] = self.mass * (self.vx*targetX - self.vx/self.tau)
            drive[1] = self.mass * (self.vy*targetY - self.vy/self.tau)

    def hasDied(self):
        p = random.uniform(0,1)
        if p < self.dieChance:
            return True
        return False


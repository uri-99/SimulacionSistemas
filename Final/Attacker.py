#stats fijos siempre. Varía su cantidad en caso 1
from utils import *


class Attacker:

    attackerSpeed = 1.6 #m/s

    def __init__(self, x, y, size, mass):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.angle = 0
        self.size = size
        self.mass = mass
        self.isDead = False

    def move(self, dt, VIP, guards, attackers):
        granular = 0
        social = 0
        drive = 0

        for person in guards + attackers:
            dist = distanceBetween(self, person)
            if dist <= (self.size/2) + (person.size/2):
                granular += #todo formula falopa de granular
            social += #todo formula falopa social
            drive =



        #todo move attacker
        return

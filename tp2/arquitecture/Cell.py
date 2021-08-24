
'''
    C . _____ . B
     /         \
  D .     *     . A
     \         /
     E . ---- . F

 A, ..., F son las Direction
 Una celda hexagonal puede tener hasta 6 particulas
'''

class Cell:
    random = False
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.oldVectors = [False,False,False,False,False,False] #A B C D E F
        self.newVectors = [False,False,False,False,False,False]
        self.isWall = False
        self.isCorner = False #implementar en la creacion del grid
        #print("cell created")

    def __repr__(self):
        #aux = str(self.i) + " " +str(self.j)
        aux = str(self.i) + " " +str(self.j) + " " + str(self.newVectors) + "-----" + str(self.oldVectors) + "\n"
        return aux

    def collisionNumber(self):
        i = 0
        for vector in self.oldVectors:
            if vector:
                i += 1
        return i

    def amountParticles(self, left):
        amount = 0
        letter = 0
        if self.j == 101:
            for vector in self.oldVectors:
                if left and ( letter == 1 or letter == 2 or letter == 3 ):
                    amount += 1    
                else:
                    if letter == 0 or letter == 4 or letter == 5 :
                        amount += 1
                letter =+ 1
        else:
            for vector in self.oldVectors:
                if vector:
                    amount += 1
        
        return amount
        
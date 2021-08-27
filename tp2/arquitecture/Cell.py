
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
        aux=""
        if self.isWall:
            aux += "\t\tWall  : "
        if self.isCorner:
            aux += "\t\tCorner: "
        aux += str(self.i) + " " +str(self.j) + " " 
        
        for i in range(5):
            if self.oldVectors[i]:
                aux+=" 1 "
            else:
                aux+=" 0 "
        aux += "-----new:"

        for i in range(5):
            if self.newVectors[i]:
                aux+=" 1 "
            else:
                aux+=" 0 "

        str(self.newVectors) + "\n"
        return aux

    def collisionNumber(self):
        i = 0
        for vector in self.oldVectors:
            if vector:
                i += 1
        return i

    def amountParticles(self, left, size):
        amount = 0
        if self.j == ((size-1)/2):
            if not left:
                for k in [0,1,5]:
                    if self.oldVectors[k]:
                        amount += 1
            else:
                for k in [2,3,4]:
                    if self.oldVectors[k]:
                        amount += 1
        else:
            for vector in self.oldVectors:
                if vector:
                    amount += 1
        
        return amount
        
from arquitecture.Cell import Cell
import random;

class Grid:
    
    def __init__(self, N, D):
        self.size = 6 #203
        self.N = N
        self.D = D
        self.cellArray = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                aux = Cell(i,j)
                if i==0 or i==202 or j==0 or j==202 or j==101:
                    aux.isWall = True
                row.append(aux)
            self.cellArray.append(row)

        #print(self.cellArray)
        #self.generateVectors(N) #tiene que quedar en init
        #print(self.cellArray)
        #print("\n\n")
        #self.generateMovements() #es pasar de t0 a t1
        #print(self.cellArray)


    def generateVectors(self, N):
        i=0
        while i<N:
            auxRow = random.choice(self.cellArray)
            auxCell = random.choice(auxRow)
            auxDir = random.randrange(0, 5, 1)
            if auxCell.newVectors[auxDir] == False:
                auxCell.newVectors[auxDir] = True
                i += 1

    
    def generateMovements(self): #transformo los new del actual a los old del vecino correspondiente
        for i in range(self.size):
            for j in range(self.size):
                #for k in self.cellArray[i][j].newVectors:
                if self.cellArray[i][j].newVectors[0]: #A
                    self.cellArray[i][j+1].oldVectors[0] = True

                if self.cellArray[i][j].newVectors[1]: #B
                    self.cellArray[i-1][j].oldVectors[1] = True

                if self.cellArray[i][j].newVectors[2]: #C
                    self.cellArray[i-1][j-1].oldVectors[2] = True

                if self.cellArray[i][j].newVectors[3]: #D
                    self.cellArray[i][j-1].oldVectors[3] = True

                if self.cellArray[i][j].newVectors[4]: #E
                    self.cellArray[i+1][j-1].oldVectors[4] = True

                if self.cellArray[i][j].newVectors[5]: #F
                    self.cellArray[i+1][j].oldVectors[5] = True

                self.cellArray[i][j].newVectors = [False, False, False, False, False, False]
                

    def calculateCollisions(self): #transformo los old actual a los new actual de cada celda
        r = random.randrange(0,1,1)
        for i in range(self.size):
            for j in range(self.size):
                if self.cellArray[i][j].collisionNumber() == 0:
                    self.cellArray[i][j].newVectors[k] = [False, False, False, False, False, False]

                if self.cellArray[i][j].collisionNumber() == 1:
                    for k in range(5):
                        self.cellArray[i][j].newVectors[k] = self.cellArray[i][j].oldVectors[k]

                if self.cellArray[i][j].collisionNumber() == 2: #tiene 3 casos

                    particle1=0
                    particle2=0
                    first = True
                    
                    for k in range(5):
                        if self.cellArray[i][j].oldVectors[k] and first:
                            particle1 = k
                            first = False
                        elif self.cellArray[i][j].oldVectors[k]:
                            particle2 = k
                            
                    case=particle2-particle1
                    if case==3: #frontal
                        if r:
                            self.cellArray[i][j].newVectors[particle1-1] = True
                            self.cellArray[i][j].newVectors[particle2-1] = True        
                        else:
                            if particle2 == 5:
                                particle2 = -1
                            self.cellArray[i][j].newVectors[particle1+1] = True
                            self.cellArray[i][j].newVectors[particle2+1] = True

                    else:
                        self.cellArray[i][j].newVectors[particle1] = True
                        self.cellArray[i][j].newVectors[particle2] = True
                    
        
                #if self.cellArray[i][j].collisionNumber() == 3:

                #if self.cellArray[i][j].collisionNumber() == 4:

                if self.cellArray[i][j].collisionNumber() == 5:
                    for k in range(5):
                        self.cellArray[i][j].newVectors[k] = self.cellArray[i][j].oldVectors[k]

                self.cellArray[i][j].oldVectors[k] = [False, False, False, False, False, False]



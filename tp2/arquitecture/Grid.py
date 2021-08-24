from arquitecture.Cell import Cell
import random;
import math;

class Grid:
    
    def __init__(self, N, D):
        self.size = 2 #203
        self.N = N
        self.D = D
        self.finishCounter = 0 # si llega a 10 el juego termino
        self.cellArray = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                aux = Cell(i,j)
                if i==0 or i==202 or j==0 or j==202 or j==101:
                    aux.isWall = True
                if (i==0 and (j==0 or j==101 or j==202)) or (i==202 and (j==0 or j==101 or j==202)):
                    aux.isWall = False
                    aux.isCorner = True
                row.append(aux)
            self.cellArray.append(row)

        #print(self.cellArray)
        self.generateVectors(N) #tiene que quedar en init
        #print(self.cellArray)
        #print("\n\n")
        #self.generateMovements() #es pasar de t0 a t1
        #print(self.cellArray)

    def __repr__(self):
        return str(self.cellArray)


    def generateVectors(self, N):
        i=0
        while i<N:
            auxRow = random.choice(self.cellArray)
            auxCell = random.choice(auxRow)
            auxDir = random.randrange(0, 5, 1)
            if auxCell.newVectors[auxDir] == False:
                auxCell.newVectors[auxDir] = True
                i += 1


    def calculateCollisions(self): #transformo los old actual a los new actual de cada celda
        r = random.randrange(0,1,1)
        for i in range(self.size):
            for j in range(self.size):
                if self.cellArray[i][j].isWall: #can not be corner
                    for k in range(5):
                        if k==0:
                            if self.cellArray[i][j].oldVectors[0] == True:
                                self.cellArray[i][j].newVectors[3] = True
                        if k==3:
                            if self.cellArray[i][j].oldVectors[3] == True:
                                self.cellArray[i][j].newVectors[0] = True
                        if j==0 or j==(self.size-1) or j==101:#es muro lateral
                            if self.cellArray[i][j].oldVectors[1] == True:
                                self.cellArray[i][j].newVectors[5] = True
                            if self.cellArray[i][j].oldVectors[5] == True:
                                self.cellArray[i][j].newVectors[1] = True
                            if self.cellArray[i][j].oldVectors[2] == True:
                                self.cellArray[i][j].newVectors[4] = True
                            if self.cellArray[i][j].oldVectors[4] == True:
                                self.cellArray[i][j].newVectors[2] = True
                        elif i==0 or i==(self.size-1): #es techo o piso
                            if self.cellArray[i][j].oldVectors[1] == True:
                                self.cellArray[i][j].newVectors[2] = True
                            if self.cellArray[i][j].oldVectors[2] == True:
                                self.cellArray[i][j].newVectors[1] = True
                            if self.cellArray[i][j].oldVectors[4] == True:
                                self.cellArray[i][j].newVectors[5] = True
                            if self.cellArray[i][j].oldVectors[5] == True:
                                self.cellArray[i][j].newVectors[4] = True

                elif self.cellArray[i][j].isCorner: #rebota de donde vino
                    for k in range(5):
                        if self.cellArray[i][j].oldVectors[k] == True:
                            self.cellArray[i][j].newVectors[k-3] = True
   
                else:
                    if self.cellArray[i][j].collisionNumber() == 0:
                        self.cellArray[i][j].newVectors = [False, False, False, False, False, False]

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
                        
                    elif self.cellArray[i][j].collisionNumber() == 3:
                        if self.cellArray[i][j].oldVectors == [True, False, True, False, True, False]:
                            self.cellArray[i][j].newVectors = [False, True, False, True, False, True]
                        elif self.cellArray[i][j].oldVectors == [False, True, False, True, False, True]:
                            self.cellArray[i][j].newVectors = [True, False, True, False, True, False]
                        else: #2 particle frontal with spectator. Falta terminar que ta jodido
                            particle1=0
                            particle2=0
                            particle3=0
                            first = True
                            second = True
                            for k in range(5):
                                if self.cellArray[i][j].oldVectors[k] and first:
                                    particle1 = k
                                    first = False
                                elif self.cellArray[i][j].oldVectors[k] and second:
                                    particle2 = k  
                                    second = False
                                elif self.cellArray[i][j].oldVectors[k]:
                                    particle3 = k 
                            #tengo los old vectors, y ahoraa?? puedo identificar los frontales, y los giro para el lado que ambos lados esten en false.


                    elif self.cellArray[i][j].collisionNumber() == 4: #double frontal cruzado usa random, else se queda igual
                        if self.cellArray[i][j].oldVectors == [True, False, True, False, True, False]:
                            self.cellArray[i][j].newVectors = [False, True, False, True, False, True]


                    elif self.cellArray[i][j].collisionNumber() == 5:
                        for k in range(5):
                            self.cellArray[i][j].newVectors[k] = self.cellArray[i][j].oldVectors[k]
                    
                    elif self.cellArray[i][j].collisionNumber() == 6:
                        self.cellArray[i][j] = [True, True, True, True, True, True, True]

                self.cellArray[i][j].oldVectors = [False, False, False, False, False, False]

    
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
                


    def amountRight(self):
        cantidad = 0
        for i in range(self.size):
            for j in range(102):
                cantidad += self.cellArray[i][j].amountParticles(False)
        return cantidad

    def amountLeft(self):
        cantidad = 0
        for i in range(self.size):
            for j in range(102):
                cantidad += self.cellArray[i][j + 101].amountParticles(True)
        return cantidad

    def isFinish(self):
        if (self.N * 0.05 > math.fabs((self.N / 2) - self.amountLeft)) and  (self.N * 0.05 > math.fabs((self.N / 2) - self.amountRight)):
            self.finishCounter += 1
        else:
            self.finishCounter = 0
        if self.finishCounter >= 10 :
            return True
        return False
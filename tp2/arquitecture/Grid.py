from arquitecture.Cell import Cell
import random;
import math;

class Grid:
    
    def __init__(self, N, D):
        self.size = 9 #203 SIEMPRE IMPAR
        if(self.size % 2 == 0) or self.size <= 3:
            print("size siempre impar para que la cancha sea pareja, y mayor a 3")
            exit()
        self.N = N
        self.D = D
        self.finishCounter = 0 # si llega a 10 el juego termino
        self.cellArray = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                aux = Cell(i,j)
                if i==0 or i==self.size-1 or j==0 or j==self.size-1 or j==( (self.size-1) / 2):
                    aux.isWall = True
                if (i==0 and (j==0 or j==( (self.size-1) / 2) or j==self.size-1)) or (i==self.size-1 and (j==0 or j==( (self.size-1) / 2) or j==self.size-1)):
                    aux.isWall = False
                    aux.isCorner = True
                row.append(aux)
            self.cellArray.append(row)

        if D > self.size-2:
            print("D es demasiado grande")
            exit()
        elif D % 2 != 1:
            print("D debe ser impar para que sea pareja la apertura")
            exit()
        
        mid = math.ceil((self.size-2)/2)
        for k in range(math.ceil(D/2)):
            print(mid-k, mid+k)
            print(math.floor((self.size-1)/2))
            self.cellArray[ mid-k ][ math.floor((self.size-1)/2) ].isWall = False
            self.cellArray[ mid-k ][ math.floor((self.size-1)/2) ].isCorner = False
            self.cellArray[ mid+k ][ math.floor((self.size-1)/2) ].isWall = False
            self.cellArray[ mid+k ][ math.floor((self.size-1)/2) ].isCorner = False

        #print("tnull:\n")
        #print(self.cellArray)

        print("\nt0:\n")
        self.generateVectors(N) #los genero en new, me aseguré de que no se generen en wall asique no hay problema
        print("left: ", self.amountLeft())
        print("right: ", self.amountRight())
        #print(self.cellArray)

        
        

    def __repr__(self):
        return str(self.cellArray)


    def generateVectors(self, N):
        i=0
        while i<N:
            auxRow = random.choice(self.cellArray)
            auxCell = random.choice(auxRow)
            auxDir = random.randrange(0, 6, 1)
            if auxCell.isWall or auxCell.isCorner:
                continue #no generar en corners o walls
            elif auxCell.j > ((self.size-1)/2):
                continue #no generar del lado derecho
            else:
                if auxCell.newVectors[auxDir] == False:
                    auxCell.newVectors[auxDir] = True
                    i += 1


    def calculateCollisions(self): #transformo los old actual a los new actual de cada celda
        r = random.randrange(0,2,1)
        for i in range(self.size):
            for j in range(self.size):
                if self.cellArray[i][j].isWall: #no puede ser corner
                    #horizontales
                    if self.cellArray[i][j].oldVectors[0] == True:
                        self.cellArray[i][j].newVectors[3] = True
                    if self.cellArray[i][j].oldVectors[3] == True:
                        self.cellArray[i][j].newVectors[0] = True

                    if j==0 or j==(self.size-1) or j==( (self.size-1) / 2):#es muro lateral
                        if self.cellArray[i][j].oldVectors[1] == True:
                            self.cellArray[i][j].newVectors[2] = True
                        if self.cellArray[i][j].oldVectors[2] == True:
                            self.cellArray[i][j].newVectors[1] = True
                        if self.cellArray[i][j].oldVectors[5] == True:
                            self.cellArray[i][j].newVectors[4] = True
                        if self.cellArray[i][j].oldVectors[4] == True:
                            self.cellArray[i][j].newVectors[5] = True
                    elif i==0 or i==(self.size-1): #es techo o piso
                        if self.cellArray[i][j].oldVectors[1] == True:
                            self.cellArray[i][j].newVectors[5] = True
                        if self.cellArray[i][j].oldVectors[2] == True:
                            self.cellArray[i][j].newVectors[4] = True
                        if self.cellArray[i][j].oldVectors[4] == True:
                            self.cellArray[i][j].newVectors[2] = True
                        if self.cellArray[i][j].oldVectors[5] == True:
                            self.cellArray[i][j].newVectors[1] = True

                elif self.cellArray[i][j].isCorner: #rebota de donde vino
                    for k in range(6):
                        if self.cellArray[i][j].oldVectors[k] == True:
                            self.cellArray[i][j].newVectors[k-3] = True
   
                else: #is normal cell
                    if self.cellArray[i][j].collisionNumber() == 0:
                        self.cellArray[i][j].newVectors = [False, False, False, False, False, False]

                    if self.cellArray[i][j].collisionNumber() == 1:
                        for k in range(6):
                            self.cellArray[i][j].newVectors[k] = self.cellArray[i][j].oldVectors[k]

                    if self.cellArray[i][j].collisionNumber() == 2: #tiene 3 casos
                        particle1=0
                        particle2=0
                        first = True
                        for k in range(6):
                            if self.cellArray[i][j].oldVectors[k] and first:
                                particle1 = k
                                first = False
                            elif self.cellArray[i][j].oldVectors[k]:
                                particle2 = k       
                        case=particle2-particle1
                        if case==3: #frontal
                            #print("doble frontal en:", i, j)
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

                        else: #2 particle frontal with spectator
                            #print("doble frontal con espectador en:", i, j)
                            particle1=0
                            particle2=0
                            particle3=0
                            first = True
                            second = True
                            for k in range(6):
                                if self.cellArray[i][j].oldVectors[k] and first:
                                    particle1 = k
                                    first = False
                                elif self.cellArray[i][j].oldVectors[k] and second:
                                    particle2 = k  
                                    second = False
                                elif self.cellArray[i][j].oldVectors[k]:
                                    particle3 = k 
                            #tengo los old vectors, y ahoraa?? puedo identificar los frontales, y los giro para el lado que ambos lados esten en false.
                            if particle2 - particle1 == 3:
                                self.cellArray[i][j].newVectors[particle3] = True #spectator
                                if self.cellArray[i][j].oldVectors[particle1-1]==False and self.cellArray[i][j].oldVectors[particle2-1]==False:
                                    self.cellArray[i][j].newVectors[particle1-1] = True
                                    self.cellArray[i][j].newVectors[particle2-1] = True
                                elif self.cellArray[i][j].oldVectors[particle1+1]==False and self.cellArray[i][j].oldVectors[particle2+1]==False:
                                    self.cellArray[i][j].newVectors[particle1+1] = True
                                    self.cellArray[i][j].newVectors[particle2+1] = True
                                else:
                                    print("error 2 triple frontal con expectador en:", i, j)
                            elif particle3 - particle1 == 3:
                                self.cellArray[i][j].newVectors[particle2] = True #spectator
                                if self.cellArray[i][j].oldVectors[particle1-1]==False and self.cellArray[i][j].oldVectors[particle3-1]==False:
                                    self.cellArray[i][j].newVectors[particle1-1] = True
                                    self.cellArray[i][j].newVectors[particle3-1] = True
                                elif self.cellArray[i][j].oldVectors[particle1+1]==False and self.cellArray[i][j].oldVectors[particle3+1]==False:
                                    self.cellArray[i][j].newVectors[particle1+1] = True
                                    self.cellArray[i][j].newVectors[particle3+1] = True
                                else:
                                    print("error 2 frontal con expectador en:", i, j)
                            elif particle3 - particle2 == 3:
                                self.cellArray[i][j].newVectors[particle1] = True #spectator
                                if self.cellArray[i][j].oldVectors[particle2-1]==False and self.cellArray[i][j].oldVectors[particle3-1]==False:
                                    self.cellArray[i][j].newVectors[particle2-1] = True
                                    self.cellArray[i][j].newVectors[particle3-1] = True
                                elif self.cellArray[i][j].oldVectors[particle2+1]==False and self.cellArray[i][j].oldVectors[particle3+1]==False:
                                    self.cellArray[i][j].newVectors[particle2+1] = True
                                    self.cellArray[i][j].newVectors[particle3+1] = True
                                else:
                                    print("error 2 frontal con expectador en:", i, j)
                            else:
                                for k in range(6):
                                    self.cellArray[i][j].newVectors[k] = self.cellArray[i][j].oldVectors[k]
                            
                    elif self.cellArray[i][j].collisionNumber() == 4: #si es double frontal cruzado usa random, else se queda igual

                        if self.cellArray[i][j].oldVectors == [True, True, False, True, True, False]:
                            #print("cuadruple cruzado en:", i, j)
                            if r:
                                self.cellArray[i][j].newVectors = [False, True, True, False, True, True]
                            else:
                                self.cellArray[i][j].newVectors = [True, False, True, True, False, True]

                        elif self.cellArray[i][j].oldVectors == [False, True, True, False, True, True]:
                            #print("cuadruple cruzado en:", i, j)
                            if r:
                                self.cellArray[i][j].newVectors = [True, True, False, True, True, False]
                            else:
                                self.cellArray[i][j].newVectors = [True, False, True, True, False, True]

                        elif self.cellArray[i][j].oldVectors == [True, False, True, True, False, True]:
                            #print("cuadruple cruzado en:", i, j)
                            if r:
                                self.cellArray[i][j].newVectors = [True, True, False, True, True, False]
                            else:
                                self.cellArray[i][j].newVectors = [False, True, True, False, True, True]
                        #listo random con 4 particulas

                        else:
                            for k in range(6):
                                self.cellArray[i][j].newVectors[k] = self.cellArray[i][j].oldVectors[k]


                    elif self.cellArray[i][j].collisionNumber() == 5:
                        for k in range(6):
                            self.cellArray[i][j].newVectors[k] = self.cellArray[i][j].oldVectors[k]
                    
                    elif self.cellArray[i][j].collisionNumber() == 6:
                        self.cellArray[i][j] = [True, True, True, True, True, True, True]

                self.cellArray[i][j].oldVectors = [False, False, False, False, False, False]

    
    def generateMovements(self): #transformo los new del actual a los old del vecino correspondiente
        for i in range(self.size):
            for j in range(self.size):
                if i%2 == 0:
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
                elif i%2 ==1:
                    if self.cellArray[i][j].newVectors[0]: #A
                        self.cellArray[i][j+1].oldVectors[0] = True

                    if self.cellArray[i][j].newVectors[1]: #B
                        self.cellArray[i-1][j+1].oldVectors[1] = True

                    if self.cellArray[i][j].newVectors[2]: #C
                        self.cellArray[i-1][j].oldVectors[2] = True

                    if self.cellArray[i][j].newVectors[3]: #D
                        self.cellArray[i][j-1].oldVectors[3] = True

                    if self.cellArray[i][j].newVectors[4]: #E
                        self.cellArray[i+1][j].oldVectors[4] = True

                    if self.cellArray[i][j].newVectors[5]: #F
                        self.cellArray[i+1][j+1].oldVectors[5] = True


                self.cellArray[i][j].newVectors = [False, False, False, False, False, False]
                


    def amountLeft(self):
        cantidad = 0
        for i in range(self.size):
            for j in range(math.floor((self.size+1)/2)):
                cantidad += self.cellArray[i][j].amountParticles(False, self.size)
        return cantidad

    def amountRight(self):
        cantidad = 0
        for i in range(self.size):
            for j in range(math.floor((self.size + 1)/2)):
                cantidad += self.cellArray[i][j + math.floor((self.size-1)/2)].amountParticles(True, self.size)
        return cantidad

    def isFinish(self):
        if (self.N * 0.05 > math.fabs((self.N / 2) - self.amountLeft())) and (self.N * 0.05 > math.fabs((self.N / 2) - self.amountRight())):
            self.finishCounter += 1
        else:
            self.finishCounter = 0
        if self.finishCounter >= 10 :
            return True
        return False

    def printGrid(self):
        for i in range(self.size):
            print(i)
            for lap in range(3):
                for j in range(self.size):
                    if lap == 0:
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        if(self.cellArray[i][j].oldVectors[2]):
                            print("[\]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].oldVectors[1]):
                            print("[/]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        print(" ", end ="")
                    elif lap == 1:
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        if(self.cellArray[i][j].oldVectors[3]):
                            print("[-]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].oldVectors[0]):
                            print("[-]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        print(" ", end ="")
                    else:
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        if(self.cellArray[i][j].oldVectors[4]):
                            print("[/]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].oldVectors[5]):
                            print("[\]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        print(" ", end ="")
                print(" -------- ", end ="")
                for j in range(self.size):
                    if lap == 0:
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        if(self.cellArray[i][j].newVectors[2]):
                            print("[\]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].newVectors[1]):
                            print("[/]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        print(" ", end ="")
                    elif lap == 1:
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        if(self.cellArray[i][j].newVectors[3]):
                            print("[-]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].newVectors[0]):
                            print("[-]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        print(" ", end ="")
                    else:
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        if(self.cellArray[i][j].newVectors[4]):
                            print("[/]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].newVectors[5]):
                            print("[\]", end ="")
                        else:
                            print("[ ]", end ="")
                        if(self.cellArray[i][j].isWall or self.cellArray[i][j].isCorner):
                            print("*", end ="")
                        print(" ", end ="")
                print("\n", end ="")
            print("\n", end ="") 
        return


        #error en colisiones cuando:
        # dos particulas se chocan en a y f, desaparece 1. Tambien desaparece si es a y b.
        # en pared cuando entra en e, por pared pasa a f y en generatemovement pasa a la pared de abajo por colosion pasa a e y por generate movement se va afuera.
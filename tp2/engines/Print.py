from arquitecture.Cell import Cell

class Print:
    def __init__(self, matrix = []):
        self.length = len(matrix)
        self.grid = matrix


    def printGrid(self):
        for i in range (self.length):
            aux = self.grid[i]
            for j in range (self.length):
                if aux[j].isWall == True:
                    print(" ++ ")
                else:
                    print(" -- ")
        print("\n")
                
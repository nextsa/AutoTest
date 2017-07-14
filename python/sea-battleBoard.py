class Board:
    field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    a = ['  ', ' 1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    b = ['1 |', '2 |', '3 |', '4 |', '5 |', '6 |', '7 |', '8 |', '9 |', '10|']
    shipCell = 1
    def _init_(self):
        
        self.field = [[0] * size for i in range(size)]
    def printBoard(self):
        for i in range(len(self.a)):
            print(self.a[i],  end=' ')
        print('\n   ---------------------')
        for i in range(len(self.field)):
            print(self.b[i], end=' ')
            for j in range(len(self.field[i])):
                print(self.field[i][j], end=' ')
            print()

    def placeShips(self, shipDirection, size, y, x):
        i = 0
        if(shipDirection == 1):
            while(i<size):
                self.field[x - 1 + i][y - 1] = self.shipCell
                
                i += 1
        elif(shipDirection == 2):
             while(i<size):
                self.field[x - 1][y - 1 + i] = self.shipCell
                i += 1
        
    def place(self):
        i = 0
        while(i != 10):
            print("Chose what kind of ship you want to place:\n1)vertical;\n2)horizontal;")
            shipDirection = input()
            if((shipDirection != '1')and(shipDirection != '2')):
                print("Wrong direction input, try again")
                print("Chose what kind of ship you want to place:\n1)vertical;\n2)horizontal;")
                shipDirection = input()
                
            print("\nEnter ship's size:")
            size = input()
            if((int(size) < 1)or(int(size) > 4)):
                print("Wrong size input, try again")
                print("Enter ship's size:")
                shipDirection = input()

            print("Enter ship's coord:\nx = ")
            x = input()
            print("y = ")
            y = input()
            board.placeShips(int(shipDirection), int(size), int(x), int(y))

            board.printBoard()
            i += 1    

"""        emptyCell = \"   \"
        shipCell = " 1 "
        waterShipCell = "   "
        missedShot = " . "
        rightShot = " X "
"""


"""
        field = []
        for i in range(0,10):
            field.append(emptyCell)
        for z in range(0,10):
            print(field)
            \"""
            if(field[z] == 0):
                print(field)
            elif(field[z] ==1):
                print(field)
            \"""
"""

            
board = Board()
board.printBoard()
board.place()
"""
i = 0
while(i != 10):
    print("Chose what kind of ship you want to place:\n1)vertical;\n2)horizontal;")
    shipDirection = input()
    if((shipDirection != '1')and(shipDirection != '2')):
        print("Wrong size input, try again")
        print("Chose what kind of ship you want to place:\n1)vertical;\n2)horizontal;")
        shipDirection = input()
        
    print("\nEnter ship's size:")
    size = input()

    print("Enter ship's coord:\nx = ")
    x = input()
    print("y = ")
    y = input()
    board.placeShips(int(shipDirection), int(size), int(x), int(y))

    board.printBoard()
    i += 1    

"""

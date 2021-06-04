"""
Pirple Homework #7.1:
	Input and Output (I-O)
	    Tic Tac Toe
"""

Field = [
    ["   ", "   ", "   "],
    ["   ", "   ", "   "],
    ["   ", "   ", "   "],
]

def drawField():
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(str(Field[i][j])+"|", end="")
            else:
                print(Field[i][j])
        if i != 2:
            print("-----------")
def checkWin():
    def gameOver():
        for i in range(3):
            for j in range(3):
                if Field[i][j] == "   ":
                    return False
                else:
                    continue
        return True
    if Field[0][0] == Field[0][1] == Field[0][2] != "   " or \
        Field[1][0] == Field[1][1] == Field[1][2] != "   " or \
        Field[2][0] == Field[2][1] == Field[2][2] != "   " or \
        Field[0][0] == Field[1][0] == Field[2][0] != "   " or \
        Field[0][1] == Field[1][1] == Field[2][1] != "   " or \
        Field[0][2] == Field[1][2] == Field[2][2] != "   " or \
        Field[0][0] == Field[1][1] == Field[2][2] != "   " or \
        Field[0][2] == Field[1][1] == Field[2][0] != "   ":
        return True
    elif gameOver():
        return False
    else:
        return None
def playerSwap():
    global Player
    if Player == 1:
        Player = 2
    else:
        Player = 1
def choose():
    choice = input()
    while isinstance(choice, int) or isinstance(choice, float):
        print("Please insert a correct choice.\n  Yes  /  No")
        choice = input()
    while choice.lower() != "yes" and choice.lower() != "no":
        print("Please insert a correct choice.\n  Yes  /  No")
        choice = input()
    if choice.lower() == "yes":
        print("New Game Loading . . .")
        for i in range(3):
            for j in range(3):
                Field[i][j] = "   "
        drawField()
        return True
    elif choice.lower() == "no":
        print("Thank you for playing.\nFinal score was:\nPlayer 1: {}\nPlayer 2: {}".format(Score[1], Score[2]))
        return False
def takeInput():
    global Row, Col
    def checkIn(var):
        if var == "1" or var == "2" or var == "3":
            return True
        else:
            print("Please enter a value between 1 and 3.")
            return False
    InputRow = input("Row:\n")
    while not checkIn(InputRow):
        InputRow = input()
    Row = int(InputRow) - 1
    InputCol = input("Column:\n")
    while not checkIn(InputCol):
        InputCol = input()
    Col = int(InputCol) - 1
    return Row, Col

Player = 1
Score = {
    1: 0,
    2: 0
}
drawField()
Row = 0
Col = 0

while True:
    print("It is Player {}'s turn.\n".format(Player))
    takeInput()
    if Field[Row][Col] != "   ":
        print("Please select an empty space.")
        continue
    if Player == 1:
        Sign = " X "
    else:
        Sign = " O "
    Field[Row][Col] = Sign
    drawField()
    if not checkWin():
        print("Game over --- It's a draw!\nScore: Player 1: {}, Player 2: {}\nWould you like to play a new game?".format(Score[1], Score[2]))
        if not choose():
            break
    elif checkWin():
        Score[Player] += 1
        print("Game over --- Player {} wins!\n Current score: \nPlayer 1: {}\nPlayer 2: {}"
              "\nWould you like to play a new game?".format(Player, Score[1], Score[2]))
        if not choose():
            break
    playerSwap()

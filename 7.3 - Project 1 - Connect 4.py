"""
Pirple Homework #7.3:
    Input and Output (I-O)
        Project #1:	Connect Four
"""
from termcolor import colored, cprint
import time

Field = [
    #  0      1      2      3      4      5      6
    ["   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 0
    ["   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 1
    ["   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 2
    ["   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 3
    ["   ", "   ", "   ", "   ", "   ", "   ", "   "],  # 4
    ["   ", "   ", "   ", "   ", "   ", "   ", "   "]]   # 5]
Dict = {
    "Player": 1,
    "Sign": colored(" O ","blue"),
    "Move": 0}
BreakFlag = False

def drawfield():
    print("-----------------------------")
    for i in range(6):
        print("|", end="")
        for j in range(7):
            if j == 6:
                print(str(Field[i][j]) + "|")
            else:
                print(str(Field[i][j]) + "|", end="")
        print("-----------------------------")
def gameON():
    def choose():
        choice = input("Would you like to play another game?\nYes / No\n")
        while not isinstance(choice, str):
            print("Please choose one of the presented options.\nYes / No\n")
            choice = input()
        while choice.lower() != "yes" and choice.lower() != "no":
            print("Please choose one of the presented options.\nYes / No\n")
            choice = input()
        if choice.lower() == "no":
            print("Thank you for playing.\nThe game will now exit.")
            time.sleep(0.2)
            global BreakFlag
            BreakFlag = True
            return BreakFlag
        elif choice.lower() == "yes":
            print("New game loading ...")
            time.sleep(0.2)
            for i in range(6):
                for j in range(7):
                    Field[i][j] = "   "
            drawfield()
            return True
    def win():
        for row in range(3):
            for col in range(7):
                if Field[row][col] == Field[row + 1][col] == Field[row + 2][col] == Field[row + 3][col] == Dict["Sign"]:
                    return True
        for col in range(4):
            for row in range(6):
                if Field[row][col] == Field[row][col + 1] == Field[row][col + 2] == Field[row][col + 3] == Dict["Sign"]:
                    return True
        for row in range(3):
            for col in range(4):
                if Field[row][col] == Field[row + 1][col + 1] == Field[row + 2][col + 2] == Field[row + 3][col + 3] == Dict["Sign"]:
                    return True
        for row in range(3):
            for col in range(3, 7):
                if Field[row][col] == Field[row + 1][col - 1] == Field[row + 2][col - 2] == Field[row + 3][col - 3] == Dict["Sign"]:
                    return True
        return False
    def draw():
        for i in range(7):
            for j in range(8):
                if Field[i][j] == "   ":
                    return False
        return True
    def playerswap():
        if Dict["Player"] == 1:
            Dict["Player"] = 2
            Dict["Sign"] = colored(" O ","red")
        else:
            Dict["Player"] = 1
            Dict["Sign"] = colored(" O ","blue")
    def move():
        def takeinput():
            Dict["Col"] = input("Choose your column.\n")
            while not str.isdigit(Dict["Col"]):
                Dict["Col"] = input("Please choose a numeric value.")
            while int(Dict["Col"]) not in range(1, 8):
                Dict["Col"] = input("Please choose a number between 1 to 7.\n")
            Dict["Col"] = int(Dict["Col"])
            Dict["Col"] -= 1
        def findrow():
            for i in reversed(range(6)):
                if Field[i][Dict["Col"]] == "   ":
                    Field[i][Dict["Col"]] = Dict["Sign"]
                    return True
            return False
        takeinput()
        while not findrow():
            print("Cannot add more pieces here. Please select another column.")
            takeinput()
    move()
    drawfield()
    if win():
        print("Game over! Player {} wins this round!\n".format(Dict["Player"]))
        choose()
    elif draw():
        print("Game over! It's a draw!")
        choose()
    playerswap()

drawfield()
while True:
    gameON()
    if BreakFlag:
        break
    print("It's Player {}'s turn.\n".format(Dict["Player"]))



"""
Pirple Homework #7.2:
	Input and Output (I-O)
	    Notes
"""
import time
import os.path

def writeToFile(file):
    print("You may now write your notes.\nType 'Exit' in a single line once you are done.\n")
    note = input()
    while note.lower() != "exit":
        file.writelines(note)
        note = input()

def existingFile():
    def fileRead():
        with open(userInput, "r") as file:
            lines = file.readlines()
            print("\n")
            for line in lines:
                print(line, end="")
    def fileReWrite():
        with open(userInput, "w") as file:
            writeToFile(file)
    def fileAppend():
        with open(userInput, "a") as file:
            writeToFile(file)
    def fileReWriteLine():
        with open(userInput, "r") as file:
            lines = file.readlines()
            lineNum = len(lines)
            print("There are", lineNum, "lines in", userInput, ".txt.")
            optionLine = int(input("Which line would you like to rewrite?\n"
                                    "Note: Please write a number from 1 to {}.\n".format(lineNum)))
            optionNote = input("Line selected. You may now rewrite the line of notes.\n")
            lines[optionLine-1] = optionNote+"\n"
        with open(userInput, "w") as file:
            file.writelines(lines)
    
    while True:
        time.sleep(0.2)
        option = input("\nWhat would you like to do?\nA: Read the File.\nB: Erase and rewrite the file.\n"
                    "C: Write at the end of the file.\nD: Rewrite one of the lines.\n"
                    "Please write one letter only.\n")
        if option.upper() == "A":
            fileRead()
            break
        elif option.upper() == "B":
            fileReWrite()
            break
        elif option.upper() == "C":
            fileAppend()
            break
        elif option.upper() == "D":
            fileReWriteLine()
            break
        else:
            print("\nInvalid input.\n")
            continue
def newFile():
    print("Writing new file named",userInput,"...")
    with open(userInput, "w") as file:
        print("File open.")
        file.write(input("You may now write your notes here.\n"))
def quitQuery():
    Answer = input("\n\nAction complete.\nWhat would you like to do now?\nQuit / Continue\n")
    while str(Answer).lower() != "quit" and str(Answer).lower() != "continue" :
        Answer = input("Please choose one of the options.\nQuit / Continue\n")
    if Answer.lower() == "quit":
        print("Now extining program.")
        time.sleep(0.2)
        return True
    elif Answer.lower() == "continue":
        return False

while True:
    userInput = input("Please enter the name of the file you wish to open.\n")+".txt"
    if os.path.isfile(userInput):
        existingFile()        
    else:
        newFile()
    if quitQuery():
        break
    print("\n")

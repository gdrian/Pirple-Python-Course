"""
Pirple Homework #7.2:
	Input and Output (I-O)
	    Notes
"""
import time
import os.path

while True:
    userInput = input("Please enter the name of the file you wish to open.\n")+".txt"
    if os.path.isfile(userInput):
        while True:
            time.sleep(0.2)
            option = input("\nWhat would you like to do?\nA: Read the File.\nB: Erase and rewrite the file.\n"
                           "C: Write at the end of the file.\nD: Rewrite one of the lines.\n"
                           "Please write one letter only.\n")
            if option.upper() == "A":
                with open(userInput, "r") as file:
                    lines = file.readlines()
                    print("\n")
                    for line in lines:
                        print(line, end="")
                break
            elif option.upper() == "B":
                with open(userInput, "w") as file:
                    file.write(input("You may now write your notes.\n")+"\n")
                    break
            elif option.upper() == "C":
                with open(userInput, "a") as file:
                    file.write(input("You may now write your notes.\n")+"\n")
                break
            elif option.upper() == "D":
                with open(userInput, "r") as file:
                    lines = file.readlines()
                    lineNum = len(lines)
                    print("There are", lineNum, "lines in", userInput, ".txt.")

                    optionLine = int(input("Which line would you like to rewrite?\n"
                                           "Note: Please write a number from 1 to {}.\n".format(lineNum)))
                    optionNote = input("Line selected. You may now write your notes.\n")
                    lines[optionLine-1] = optionNote+"\n"
                with open(userInput, "w") as file:
                    file.writelines(lines)
                break
            else:
                print("The option you have selected is incorrect.\nPlease write either A, B, C or D.")
                continue
    else:
        print("Writing new file named",userInput,"...")
        with open(userInput, "w") as file:
            print("File open.")
            file.write(input("You may now write your notes here.\n"))

    Action = input("\n\nAction complete.\nWhat would you like to do now?\nQuit / Continue\n")
    while str.isdigit(Action):
        Action = input("Please choose one of the options.\nQuit / Continue\n")
    while Action.lower() != "quit" and Action.lower() != "continue" :
        Action = input("Please choose one of the options.\nQuit / Continue\n")
    if Action.lower() == "quit":
        print("Now extining program.")
        time.sleep(0.2)
        break
    elif Action.lower() == "continue":
        continue
    print("\n")

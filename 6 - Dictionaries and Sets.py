'''
Pirple Homework #6:
	Dictionaries and Sets

Return to your first homework assignments, when you described your favorite song. Refactor that code so all the
	variables are held as dictionary keys and value. Then refactor your print statements so that it's a single
	loop that passes through each item in the dictionary and prints out it's key and then it's value.

Extra Credit:
Create a function that allows someone to guess the value of any key in the dictionary, and find out if they
	were right or wrong. This function should accept two parameters: Key and Value. If the key exists in the
	dictionary and that value is the correct value, then the function should return true. In all other cases,
	it should return false.
'''

import time
time.sleep(1)

# Definitions and Variables

Dictionary = {
	"SongName": "Turn The Page",
	"Genre": "Metal",
	"Artist": "Metallica",
	"ReleaseDate": 1998,
	"DurMin": 5.833,
	"DurSec": 350}
Question = {
	"SongName": "What is the name of the song we are discussing today?\n",
	"Genre": "What genre is the song part of?\n",
	"Artist": "What is the name of the band who covered the song?\n",
	"ReleaseDate": "When was the album released?\n",
	"DurMin": "In minutes, how long is the song precisely?\n",
	"DurSec": "In seconds, how long is the song precisely?\n"}
breakflag = False

def game():
	def tryAgain():
		answer = input("Would you like to try again?\nYes / No\n")
		while answer.lower() != "yes" and answer.lower() != "no":
			answer = input("Please choose a correct answer. \nYes / No\n")
		if str(answer).lower() == "yes":
			print("New game starting . . .")
			time.sleep(0.5)
			return True
		elif str(answer).lower() == "no":
			print("Thank you for playing. Game will now quit.")
			time.sleep(0.5)
			global breakflag
			return False
	def qna():
		Score = 0
		for key in Dictionary:
			val = Dictionary[key]
			answer = input(Question[key])
			if answer.lower() == str(val).lower():
				print("You are correct!\n")
				Score += 1
			else:
				print("Close. The correct answer was {}.\nYour final score was {}.\n".format(val, Score))
				if not tryAgain():
					global breakflag
					breakflag = True
					break
	qna()

while True:
	if breakflag:
		break
	game()

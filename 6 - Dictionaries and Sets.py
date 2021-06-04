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

def gamecheck():
	Score = 0
	for key in Dictionary:
		val = Dictionary[key]
		print(Question[key])
		answer = input()
		if isinstance(val, float):
			if float(answer) == val:
				print("You are correct!")
				Score += 1
				continue
			else:
				print("Close. The correct answer was {}.\nYour final score was {}.\nWould you like to try again?\n  Yes  /  No  ".format(val, Score))
				answer = input()
				while answer.lower() != "no" and answer.lower() != "yes":
					print("Please insert a correct value: Yes / No")
					answer = input()
				if answer.lower() == "no":
					print("Thank you for playing.\nGame will now quit.")
					time.sleep(1)
					return False
				elif answer.lower() == "yes":
					print("Game loading . . .")
					time.sleep(0.8)
					return True
		elif isinstance(val, int):
			if int(answer) == val:
				print("You are correct!")
				Score += 1
				continue
			else:
				print(
					"Close. The correct answer was {}.\nYour final score was {}.\nWould you like to try again?\n  Yes  /  No  ".format(
						val, Score))
				answer = input()
				while answer.lower() != "no" and answer.lower() != "yes":
					print("Please insert a correct value: Yes / No")
					answer = input()
				if answer.lower() == "no":
					print("Thank you for playing.\nGame will now quit.")
					time.sleep(1)
					return False
				elif answer.lower() == "yes":
					print("Game loading . . .")
					time.sleep(0.8)
					return True
		else:
			if answer.lower() == val.lower():
				print("You are correct!")
				Score += 1
				continue
			else:
				print("Close. The correct answer was {}.\nYour final score was {}.\nWould you like to try again?\n  Yes  /  No  ".format(val, Score))
				answer = input()
				while answer.lower() != "no" and answer.lower() != "yes":
					print("Please insert a correct value: Yes / No")
					answer = input()
				if answer.lower() == "no":
					print("Thank you for playing.\nGame will now quit.")
					time.sleep(1)
					return False
				elif answer.lower() == "yes":
					print("Game loading . . .")
					time.sleep(0.8)
					return True



while True:
	if gamecheck():
		continue
	else:
		break

'''
Pirple Homework #3:
	"If" Statements.

Create a function that accepts 3 parameters and checks for equality between any two of them.
Your function should return True if 2 or more of the parameters are equal,
	and false is none of them are equal to any of the others.

Extra Credit:
Modify your function so that strings can be compared to integers if they are equivalent.
'''

A = 5
B = 5.5
C = "5"

if A == B == int(C):
	print ("The three numerical entries are equal to each other.")
elif A == B or A == int(C) or B == int(C):
	print ("Two of the numerical entries are equal to each other.")
else:
	print ("All three numerical entries are unique to each other.")

'''
Attempting to learn how to use input with the same exercise.

D = int(input ("The first number is: "))
E = int(input ("The second number is: "))
F = int(input ("The final number is:"))

if D == E == F:
	print ("You have entered the same number three times.")
elif D == E or D == F or E == F:
	print ("Two numbers are duplicated.")
else:
	print ("The numbers entered are unique.")
'''
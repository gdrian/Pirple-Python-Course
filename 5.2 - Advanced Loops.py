'''
Pirple Homework #5.2:
	Loops
	    Advanced Loops

Create a function that takes in two parameters: rows, and columns, both of which are integers.
The function should then proceed to draw a playing board the same number of rows and columns as specified.
After drawing the board, your function should return True.

Extra Credit:
Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping.
If someone passes a value greater than either maximum, your function should return False.
'''


print("\n")
RowNum = int(input("Input number of rows: "))*2-1
ColNum = int(input("Input number of columns: "))*2-1
RowMax = 20
ColMax = 25
print("\n")

def drawTable(Row,Col):
	for row in range(RowNum):
		if row % 2 == 0:
			for col in range(ColNum):
				if col % 2 == 0:
					if col != (ColNum-1):
						print(" ", end = "")
					else:
						print(" ")
				elif col != (ColNum-1):
						print("|", end = "")
				else:
					print("|")
		else:
			print("-" * ColNum)
	if RowNum<=RowMax and ColNum <= ColMax:
		return True
	else:
		return False


if drawTable(RowNum, ColNum):
	print("\nEverything seems to be fine here.")
else:
	print("\nThe table you are trying to insert is too large for my terminal. Not sure about yours though!")
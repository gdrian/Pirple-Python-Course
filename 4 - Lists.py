'''
Pirple Homework #4:
	Lists

Create a global variable called myUniqueList. It should be an empty list to start.
Next, create a function that allows you to add things to that list.
Anything that's passed to this function should get added to myUniqueList,unless its value already exists in
	myUniqueList. If the value doesn't exist already, it should be added and the function should return True.
	If the value does exist, it should not be added, and the function should return False;

Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the
	different scenarios, and then finally it should print the value of myUniqueList to show that it worked.


Extra Credit:
Add another function that pushes all the rejected inputs into a separate global array called myLeftovers.
If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness),	it should get added
	to myLeftovers instead.
'''

myUniqueList = []
myLeftovers = []

print("Please ")

while True:
    Input = input("Insert a new value:\n")
    if Input.lower() == "stop":
        break
    elif Input in myUniqueList:
        myLeftovers.append(Input)
    else:
        myUniqueList.append(Input)

print("\nUnique Values inserted:")

count = 0
for i in myUniqueList:
    count += 1

for i in range(count):
    if i == count-1:
        print("and", str(myUniqueList[i])+".")
    else:
        print(str(myUniqueList[i])+", ", end = "")

print("\nDuplicate Values inserted:")
print(myLeftovers)

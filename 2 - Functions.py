'''
Pirple Homework #2:
	Functions.

Let's return to the music example from assignment one. Pick 3 of the attributes you listed.
For our example we're going to say "Genre", "Artist" and "Year".
Create a new Python file and create 3 functions with the same name as those attributes.

When someone calls any of those functions, that function should return the corresponding value for that attribute.

Extra Credit:
One of the data types we haven't covered yet is called "booleans".
For extra credit, see if you can figure out how to use booleans,and add an extra function that returns a boolean
	value instead of a String or Number.
'''

SongName = "Turn The Page"
Genre = "Metal"
Artist = "Metallica"

def check(Var):
	if Var == "Metal":
		return True

def output():
	print("Artist name: {}".format(Artist))
	print("Song name: {}".format(SongName))
	if check(Genre):
		print("Genre: {}".format(Genre))

output()
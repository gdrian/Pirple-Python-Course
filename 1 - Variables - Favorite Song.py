'''
Pirple Homework #1:
	Variables.
	    Favorite Song

What's your favorite song?

Think of all the attributes that you could use to describe that song.
These are attributes like "Artist", "Year Released", "Genre", "Duration", etc.
Now, within that file, list all of the attributes of the song, one after another,
    by creating variables for each attribute, and giving each variable a value.
Give each variable its own line. Then, after you have listed the variables, print each one of them out.
'''

# 1. Defining Variables

SongName = "Turn The Page"
Genre = "Metal"
Artist = "Metallica"
AlbumName = "Garage Inc."
ReleaseDate = 1998
DurationInMinutes = 5.833
DurationInSeconds = 350
Chours = "Here I am, on the road again\nThere I am, up on the stage\n" \
         "Here I go playin' the star again\nThere I go, turn the page"

# 2. Output
print ("{} - {}\n".format(Artist, SongName))
print ("Album Name: {}, released in {}".format(AlbumName,ReleaseDate))
print ("Genre: ", Genre)
print ("Duration: {} minutes or {} seconds.".format(DurationInMinutes, DurationInSeconds))
print ("Chours:\n", Chours)
class Song:
    # constructor to set initial values
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    # __str__ method returns formatted string of song data
    def __str__(self):
        return (f"Performer: {self.artist}\n"
                f"Title:     {self.title}\n"
                f"Album:     {self.album}\n"
                f"Year:      {self.year}")

# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

# object usage
print(song1)
print()  # empty line between songs
print(song2)

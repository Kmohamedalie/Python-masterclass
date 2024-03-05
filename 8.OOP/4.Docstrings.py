# *********************************************************************
#               Docstrings: Class to represent songs                  #
# *********************************************************************

class Song:
    """Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator.
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):

        self.title = title
        self.artist = artist
        self.duration = duration


# help(Song)
help(Song.__init__)
help(Song.__doc__)
help(Song.__init__.__doc__)
Song.__init__.__doc__ = """ Song init method

        :param title (str): Initalises the 'title' attribute
        :param article (Artist): At Artist object representing the song's creator.
        :param duration (Optional[int]: Initial value for the 'duration' attribute.
               will default to zero if not specified.
        """
help(Song)

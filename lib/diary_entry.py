class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents
        self.bookmark = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return self.count_words() / wpm

        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        

    def reading_chunk(self, wpm, minutes):
        if self.bookmark >= len(self.contents):
            self.bookmark = 0
        words_to_read = wpm * minutes
        list_of_words = self.contents.split()[self.bookmark:self.bookmark+ words_to_read]
        self.bookmark += words_to_read
        return " ".join(list_of_words)
        

        # for entry in self.entries:
        #     if words_to_read <= self.count_words():
        #         return entry.title
            
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        
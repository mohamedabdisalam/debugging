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

    def reading_chunk(self, wpm, minutes):
        if self.bookmark >= self.count_words() -1:
            self.bookmark = 0
        words_to_read = wpm * minutes
        list_of_words = self.contents.split()[self.bookmark:self.bookmark+ words_to_read]
        self.bookmark += words_to_read
        return " ".join(list_of_words)
    
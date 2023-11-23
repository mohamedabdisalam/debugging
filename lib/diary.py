from lib.diary_entry import *
class Diary:
    def __init__(self):
        self.entries = []
    
    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        length_of_diary = 0
        for char in self.entries:
            length_of_diary += char.count_words()
        return length_of_diary

    def reading_time(self, wpm):
        return self.count_words() / wpm

    def find_best_entry_for_reading_time(self, wpm, minutes):
        number_of_words_to_read = wpm * minutes
        my_dictionary = {}
        for entry in self.entries:
            if entry.count_words() <= number_of_words_to_read:
                my_dictionary[entry] = entry.count_words()
        best_match = sorted(my_dictionary.items(), key=lambda item: item[1])[-1][0]
        return best_match.title


        # for entry in self.entries:
        #     if number_of_words_to_read <= self.count_words():
        #         return entry.title


        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        



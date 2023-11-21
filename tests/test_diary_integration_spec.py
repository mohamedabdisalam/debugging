from lib.diary import *
from lib.diary_entry import *

""""
Test the init statement
"""

def test_diary_initialiser():
    diary = Diary()
    assert isinstance(diary, Diary)

"""
Given an entry add it
To the diary
"""
def test_adding_to_diary():
    diary = Diary()
    diary.add("Today was a good day")
    expected = ["Today was a good day"]
    actual = diary.entries
    assert expected == actual

"""
Returns a list of instances of DiaryEntry
"""
def test_show_entries():
    diary = Diary()
    diary.add("Today was a good day")
    diary.add("Mohamed and Liam paired")
    expected = ["Today was a good day", "Mohamed and Liam paired"]
    actual = diary.all()
    assert expected == actual

"""
Returns number of words in diary entry class
"""
def test_count_number_of_words_in_diary_entry():
    diary_entry = DiaryEntry("Tuesday", "Today was a good day")
    expected = 5
    actual = diary_entry.count_words()
    assert expected == actual
"""
Returns number of words in diary class
"""
def test_count_number_of_words_in_diary():
    diary = Diary()
    diary.add("Today was a good day")
    expected = 5
    actual = diary.count_words
    assert expected == actual

"""
Given WPM as an integer 
Returns estimate of time if the user was to
Read all the diary
"""

"""
Given WPM as an integer
Given the number of minutes the user has
Returns instance of diary entry representing
The diary entry that is closest to 
but not over the length that the user could read
in the available minutes
"""
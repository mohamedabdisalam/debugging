from lib.diary import *
from lib.diary_entry import *

""""
Test the init statement
"""

# def test_diary_initialiser():
#     diary = Diary()
#     assert isinstance(diary, Diary)

"""
Given an entry add it
To the diary
"""
def test_adding_to_diary_and_returning_the_list():
    diary = Diary()
    # diary_entry = DiaryEntry
    entry1 = DiaryEntry("Title 1", "Today was a good day")
    entry2 = DiaryEntry("Title2", "Today was a bad day")
    diary.add(entry1)
    diary.add(entry2)
    expected = [entry1, entry2]
    actual = diary.all()
    assert expected == actual

"""
Returns a list of instances of DiaryEntry
"""
# def test_show_entries():
#     diary = Diary()
#     diary.add("Today was a good day")
#     diary.add("Mohamed and Liam paired")
#     expected = ["Today was a good day", "Mohamed and Liam paired"]
#     actual = diary.all()
#     assert expected == actual

"""
Returns number of words in diary entry class
"""
# def test_count_number_of_words_in_diary_entry():
#     diary_entry = DiaryEntry("Tuesday", "Today was a good day")
#     expected = 5
#     actual = diary_entry.count_words()
#     assert expected == actual
"""
Returns number of words in diary class
"""
def test_count_number_of_words_in_diary():
    diary = Diary()
    entry1 = DiaryEntry("Title1", "Today was a good day")
    entry2 = DiaryEntry("Title2", "Today was a bad day")
    diary.add(entry1)
    diary.add(entry2)
    expected = 10
    actual = diary.count_words()
    assert expected == actual

"""
Given WPM as an integer 
Returns estimate of time if the user was to
Read all the diary
"""

def test_estimate_time_to_read_whole_diary():
    diary = Diary()
    entry1 = DiaryEntry("Title1", "Today was a good day")
    entry2 = DiaryEntry("Title2", "Today was a bad day")
    diary.add(entry1)
    diary.add(entry2)
    expected = 1
    actual = diary.reading_time(10)
    assert expected == actual

"""
Given WPM as an integer
Given the number of minutes the user has
Returns instance of diary entry representing
The diary entry that is closest to 
but not over the length that the user could read
in the available minutes
"""

def test_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry("Title1", "Today was a good day")
    entry2 = DiaryEntry("Title2", "One Two Three Four Five Siz Seven Eight Nine Ten")
    diary.add(entry1)
    diary.add(entry2)
    expected = "Title1"
    actual = diary.find_best_entry_for_reading_time(5, 1)
    assert expected == actual

def test_best_entry_for_reading_time_longer():
    diary = Diary()
    entry1 = DiaryEntry("Title1", "Today was a good day Today was a good day Today was a good day Today was a good day Today was a good day")
    entry2 = DiaryEntry("Title2", "One Two Three Four Five Siz Seven Eight Nine Ten")
    diary.add(entry1)
    diary.add(entry2)
    expected = "Title2"
    actual = diary.find_best_entry_for_reading_time(10, 1)
    assert expected == actual
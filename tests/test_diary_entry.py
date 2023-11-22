from lib.diary_entry import *

def test_count_number_of_words_in_individual_entry_to_contents():
    diary_entry = DiaryEntry("Tuesday", "Today was a good day")
    expected = 5
    actual = diary_entry.count_words()
    assert expected == actual

def test_reading_time_based_on_given_int():
    diary_entry = DiaryEntry("Tuesday", "Today was a good day")
    expected = 1
    actual = diary_entry.reading_time(5)
    assert expected == actual
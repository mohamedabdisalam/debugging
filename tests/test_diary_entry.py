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

def test_give_a_chunk_of_text_we_can_read_in_given_time():
    diary_entry = DiaryEntry("Tuesday", "Today was a good day six seven eight nine ten")
    expected = "Today was a good day"
    actual = diary_entry.reading_chunk(5, 1)
    assert expected == actual

def test_give_a_chunk_of_text_we_can_read_in_given_time_longer():
    diary_entry = DiaryEntry("Tuesday", "Today was a good day six seven eight nine ten")
    expected = "six seven eight nine ten"
    actual = diary_entry.reading_chunk(5, 1)
    assert expected == actual
from lib.diary import *

def test_diary_initialiser():
    diary = Diary()
    assert isinstance(diary, Diary)


def test_show_entries_within_the_list():
    diary = Diary()
    diary.add("Today was a good day")
    diary.add("Mohamed and Liam paired")
    expected = ["Today was a good day", "Mohamed and Liam paired"]
    actual = diary.all()
    assert expected == actual


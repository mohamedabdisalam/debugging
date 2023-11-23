from lib.todo import *

"""
Test initialiser is initialising
"""

def test_initialiser():
    todo = Todo("")
    assert isinstance(todo, Todo)

def test_task_showing_the_task():
    todo = Todo("Going to the gym")
    expected = "Going to the gym"
    actual = todo.task
    assert expected == actual

"""
Test that task = false
"""

def test_task_is_false_by_default():
    todo = Todo("Going to the gym")
    expected = False
    actual = todo.complete
    assert expected == actual


"""
Given a task
We want to mark it as complete
The state should be True
"""

def test_task_is_marked_as_complete():
    task1 = Todo("Going to the gym")
    task1.mark_complete()
    expected = True
    actual = task1.complete
    assert expected == actual

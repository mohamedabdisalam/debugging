from lib.todo_list import *

"""
Test initialiser is initialising
"""

def test_initialiser():
    todo_list = TodoList()
    assert isinstance(todo_list, TodoList)

"""
Given we are adding a task 
Returns nothing
Sideffect task is added to the list
"""

def test_add_a_new_task_to_the_list():
    todo_list = TodoList()
    todo_list.add("Go the the gym")
    expected = ["Go the the gym"]
    actual = todo_list.task_list
    assert expected == actual 


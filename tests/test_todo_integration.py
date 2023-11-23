from lib.todo_list import *
from lib.todo import *

"""
Given we are adding a task 
The task should be in the dictionary
Returns nothing
Default should be false 
"""

def test_add_a_new_task_to_the_list():
    todo_list = TodoList()
    entry1 = Todo("Go the the gym")
    entry2 = Todo("Finish test driving a class system")
    todo_list.add(entry1)
    todo_list.add(entry2)
    expected = [entry1, entry2]
    actual = todo_list.task_list
    assert expected == actual


"""
Given a list of tasks
Return the list of items that are incomplete

"""

def test_return_a_list_of_incomplete_tasks():
    todo_list = TodoList()
    todo1 = Todo("Going to the gym")
    todo2 = Todo("Going to the shop")
    todo_list.add(todo1)
    todo_list.add(todo2)
    expected = [todo1, todo2]
    actual = todo_list.incomplete()
    assert actual == expected

"""
Given we have a list of tasks
When we complete a task
#complete returns a list of 
Completed tasks
"""

def test_return_a_list_of_completed_tasks():
    todo_list = TodoList()
    todo1 = Todo("Going to the gym")
    todo2 = Todo("Going to the shop")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo1.mark_complete()
    expected = [todo1]
    actual = todo_list.complete()
    assert actual == expected




def test_marks_all_tasks_in_list_as_complete():
    todo_list = TodoList()
    todo1 = Todo("Going to the gym")
    todo2 = Todo("Going to the shop")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.give_up()
    expected = [todo1, todo2]
    actual = todo_list.complete()
    assert actual == expected

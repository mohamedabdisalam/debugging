from lib.todo_list import *
from lib.todo import *

"""
Instantiate the class
With an empty list
"""

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
    actual = todo_list.incomplete()
    assert expected == actual

"""
Given we have a list of tasks
When we complete a task
#complete returns a list of 
Completed tasks
"""

def test_return_a_list_of_completed_taks():
    todo_list = TodoList()
    entry1 = Todo("Go the the gym")
    entry2 = Todo("Finish test driving a class system")
    entry1.mark_complete()
    todo_list.add(entry1)
    todo_list.add(entry2)
    expected = []
    actual = todo_list.complete() #ret
    assert expected == actual

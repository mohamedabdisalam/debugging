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

# def test_return_a_list_of_incomplete_tasks():
#     todo_list = TodoList()
#     entry1 = todo_list.add("Go the the gym")
#     entry2 = todo_list.add("Go the the shop")
#     entry3 = todo_list.add("Go the the hospital")
#     expected = [entry1, entry2, entry3]
#     actual = todo_list.incomplete()
#     assert expected == actual 

"""
Given we have a list of tasks
When we complete a task
#complete returns a list of 
Completed tasks
"""

# def test_return_a_list_of_completed_taks():
#     todo_list = TodoList()
#     entry1 = Todo("Go the the gym")
#     entry2 = Todo("Finish test driving a class system")
#     entry1.mark_complete()
#     todo_list.add(entry1)
#     todo_list.add(entry2)
#     expected = []
#     actual = todo_list.complete() #ret
#     assert expected == actual


 
from lib.todo_list import *
from lib.todo import *

"""
Given we are adding a task 
The task should be in the dictionary
Returns nothing
Default should be false 
"""

def test_add_a_new_task_to_the_dictionary_as_false():
    todo_list = TodoList()
    entry1 = Todo("Go the the gym")
    entry2 = Todo("Go the the gym")

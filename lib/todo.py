from lib.todo_list import *

class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        self.task = task
        self.complete = False

        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        #Sets any property to false

    def mark_complete(self):
        self.complete = True
        
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        

        
    #Might need to iterate through 
    # the list to cross check those that are complete
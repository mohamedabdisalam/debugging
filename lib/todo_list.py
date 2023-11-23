class TodoList:
    def __init__(self):
        self.task_list = []
        # self.incomplete = False
        self.complete = True

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.task_list.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        # for task in self.task_list:
        #     if task == s:
        #         return task
        return self.task_list

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass



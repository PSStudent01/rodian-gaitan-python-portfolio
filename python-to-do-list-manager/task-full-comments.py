'''
Task class for the to-do list manager.
A Task holds a title, an optional due date (a datetime.date object or a string), and a completed flag. Its __str__ method returns 
a readable line such as "[-] Task: Submit assignment (due 2025-03-10)", where [X] marks a completed task and [-] marks one that 
is still open.
'''

class Task:  # 1) Defining class 'Task'...
    def __init__(self, title, due_date=None, completed=False): # 2)...with attributes and an initializer to set up those attributes.
        self.title = title # setting up 'instance attribute assignment' for attribute 'title'
        self.due_date = due_date # setting up 'instance attribute assignment' for attribute 'due_date'
        self.completed = completed  # setting up 'instance attribute assignment' for attribute 'completed'

    # Methods:
    def __str__(self):
        if self.completed is False: # If the condition is true (iows, 'not completed')
            return f"[-] Task: {self.title} (due {self.due_date})" # then it returns the task with [-] to indicate it is incomplete. 
        elif self.completed is True: # Otherwise, if the condition is true (iows, 'complete'),
            return f"[X] Task: {self.title} (due {self.due_date})" # then it returns the task with [X] to indicate it is complete.

if __name__ == "__main__":  # It allows the code inside the if block to run when this file is executed directly (meaning from inside this file,), 
                            # but prevents that code from running when another script imports this file as a module.

    print("============================= Personal To-Do List Manager ============================== \n") # prints a title banner, plus a blank line from the '\n'
    task_1 = Task("'ALAB 356.4 - Generators, Closures, and Utility Methods'", "2026-11-20", True) # a completed task: all 3 arguments given, so it prints with [X]
    task_2 = Task("'SBA 356 - Python Essentials 2'", "2026-11-20", False) # an incomplete task: 'completed' passed explicitly as False, so it prints with [-]
    task_3 = Task("'KBA 356 - Python Essentials 2'", "2026-11-20", False) # a second incomplete task, same pattern as task_2
    task_4 = Task("'End of Course Survey'", "2026-11-20", False) # 'completed' passed explicitly as False
    task_5 = Task("'End of Course Survey'", "2026-11-20")  # 'completed' left out, so it falls back to its default (False). Prints the same as task_4
    task_6 = Task("'End of Course Survey'") # 'due_date' and 'completed' both left out, so both use their defaults. Interesting, it returns 
                                            # "[-] Task: 'End of Course Survey' (due None)".
    print(task_1) # print() calls each task's __str__() method automatically, which returns the formatted line
    print(task_2)
    print(task_3)
    print(task_4)
    print(task_5)
    print(task_6)







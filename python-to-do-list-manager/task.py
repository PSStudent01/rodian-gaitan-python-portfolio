'''
Task class for the to-do list manager.
A Task holds a title, an optional due date (a datetime.date object or a string), and a completed flag. Its __str__ method 
returns a readable representation of the task, where [X] indicates completed and [-] indicates incomplete.
'''

class Task:
    def __init__(self, title, due_date=None, completed=False):
        # Initializes the instance attributes using the supplied arguments.
        self.title = title
        self.due_date = due_date
        self.completed = completed

    # Method to return a formatted string representation of the task.
    def __str__(self):
        # Checks whether the task's completed attribute is False (incomplete).
        if self.completed is False:
            return f"[-] Task: {self.title} (due {self.due_date})"

        # Otherwise, checks whether the task's completed attribute is True (complete).
        elif self.completed is True:
            return f"[X] Task: {self.title} (due {self.due_date})"


# Runs these test examples only when this file is executed directly.
if __name__ == "__main__":

    print("============================= Personal To-Do List Manager ============================== \n")

    # Creates a completed task by explicitly passing True for the completed argument.
    task_1 = Task("'ALAB 356.4 - Generators, Closures, and Utility Methods'", "2026-11-20", True)

    # Creates incomplete tasks by explicitly passing False for the completed argument.
    task_2 = Task("'SBA 356 - Python Essentials 2'", "2026-11-20", False)
    task_3 = Task("'KBA 356 - Python Essentials 2'", "2026-11-20", False)
    task_4 = Task("'End of Course Survey'", "2026-11-20", False)

    # Omits completed to use its default value of False.
    task_5 = Task("'End of Course Survey'", "2026-11-20")

    # Omits both optional arguments to use their defaults: 'None' for due_date and 'False' for completed.
    task_6 = Task("'End of Course Survey'")

    # print() automatically calls each Task object's __str__() method.
    print(task_1)
    print(task_2)
    print(task_3)
    print(task_4)
    print(task_5)
    print(task_6)
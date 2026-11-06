'''
To-do list manager functions.
Functions for adding, completing, deleting and listing Task objects, plus saving and loading the list as a CSV file. Used by main.py.
''' 

########################################  Creates a new Task and adds it to the list: ######################################
from task import Task # import class 'Task' from the module 'task' ('task.py')
from datetime import datetime, date # import 'datetime' and 'date' classes from 'datetime' module
import os # gives you ways to interact with the operating system, like files and folders. Itc, you use it for function
          # 'load_tasks' to see if the 'tasks' file exists.
import csv # used to read and write the tasks file in CSV format. 

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # A!) Grabs the directory containing this todolist.py file.
                                                      # Prevents user from manually having to cd to the project
                                                      # root folder in order to run program

def save_tasks(task_list, filename="tasks.csv"):  # [PART 1 - Saving File, see 'main.py' for PART 2] 'save tasks', meaning for
                                                  # writting-to-a-file purposes.
    filename = os.path.join(BASE_DIR, filename)  # B!) Build the full path to tasks.csv.
    try: # 1A) Exception handling for attempting to add a task and saving to a read-only 'tasks.csv' file.
        with open(filename, "w", newline="") as file: # "w" = write mode (it replaces the file). If the file exists, its old contents
                                                  #  are erased. That’s why saving the full task_list works.
                                                  # A) 'open(filename, "w", newline="")' =  opens the file named in filename.
                                                  # The "w" means write mode, so you can write/save to the file to modify/store to it. 
                                                  # B) ' newline="" ' =  is a setting the csv module recommends. It stops Python 
                                                  # from messing with line endings, so rows are written to correctly on Windows too.
                                                  # C) 'as file' =  THE RESULT of everything to the left of 'file' variable 
                                                  # is stored inside the 'file' variable , so you can use it on the lines 
                                                  # below (ex, csv.writer(file)).
                                                  # D) 'with' = is what closes the file for you. When the indented block 
                                                  # ends, Python closes the file automatically, even if an error happens 
                                                  # inside it. Without with, you’d have to remember to call file.close() 
                                                  # yourself. Everything indented under the with line is the part where the 
                                                  # file is open.
            writer = csv.writer(file) # It creates a writer object that knows how to write CSV-formatted lines into the open 
                                  # file, and names it writer.
                                  # 'csv.writer(file)' = it takes the open file object (file, from as file) and wraps it with CSV 
                                  # rules: separating values with commas, adding quotes when needed, and ending each row with
                                  # a line break.
                                  # 'writer' = that object is then stored in variable 'writer' so you can use it on the next lines.
            for task in task_list:    # this says " for each and every task in 'task_lists', do the following..."
                writer.writerow([task.title, task.due_date or "", task.completed]) # this line  writer.writerow([task.title,
                                                                               # task.due_date or "", task.completed])
                                                                               # - 'writer.writerow(...)' = tells the CSV writer 
                                                                               # to write one row. It puts commas between the 
                                                                               # items in the list and ends the line.
                                                                               # - '[task.title, task.due_date or "", 
                                                                               # task.completed] = is the list of three values that
                                                                               # make up the row, in the same order load_tasks 
                                                                               # reads them: title, due date, completed.'
                                                                               # - ' task.due_date or "" ' = handles tasks with 
                                                                               # no date. If due_date is a real date, it’s used 
                                                                               # as is. If it’s None, Python falls through to "",
                                                                               # so the row gets an empty spot instead of the 
                                                                               # text None.
                                                                               # - 'task.completed' = is 'True' or 'False', and the 
                                                                               # writer saves it as the text True or False, which
                                                                               # is what ' completed == "True" ' in load_tasks 
                                                                               # expects.
                                                                               # So this line doesn’t build an object, rather it
                                                                               # takes an object that already exists and 
                                                                               # writes its contents to the file.
    except OSError as e: # 1B) Exception handling for attempting to add a task and saving to a read-only 'tasks.csv' file.
        print(f"Error: could not save tasks ({e}).")  # 1C) Exception handling for attempting to add and saving a task to a read-only 'tasks.csv' file.

def load_tasks(filename="tasks.csv"): # 'load tasks', meaning for reading purposes.
    filename = os.path.join(BASE_DIR, filename)  # C!) Build the full path to tasks.csv.
    task_list = []
    if os.path.exists(filename):  # True if the file exists, False if it doesn't. Only load if the file (passed as argument by user)
                                 # exists. IOWS, it checks for the file. If it’s not there, you just get an empty list, which is what 
                                 # a first run should do.
        try:  ########################## Protect the actual file-reading operation
        # opens the file so your code can read it, and closes it automatically when you’re done:
            with open(filename, "r", newline="") as file: # A) 'open(filename, "r", newline="")' =  opens the file named in filename. 
                                                       # The "r" means read mode, so you can read the file but not change it. 
                                                       # ("w" would be write mode, which you’ll use in save_tasks.)
                                                       # B) ' newline="" ' =  is a setting the csv module recommends. It stops Python 
                                                       # from messing with line endings, so rows are read correctly on Windows 
                                                       # too. You can just treat it as part of the standard CSV recipe.
                                                       # C) 'as file' =  THE RESULT of everything to the left of 'file' variable 
                                                       # is stored inside the 'file' variable , so you can use it on the lines 
                                                       # below (ex, csv.reader(file)).
                                                       # D) 'with' = is what closes the file for you. When the indented block 
                                                       # ends, Python closes the file automatically, even if an error happens 
                                                       # inside it. Without with, you’d have to remember to call file.close() 
                                                       # yourself. Everything indented under the with line is the part where the 
                                                       # file is open:
                for row in csv.reader(file): # this says "for each and every row (aka item) in the open file (itc, "tasks.csv") 
                                         # inside the variable 'file', do as follows:
                        if len(row) != 3: # a) <--Temp fix to issue where updating .csv with weird charcaters and order cause crash
                            continue # b) <--Temp fix to issue where updating .csv with weird charcaters and order cause crash
                        title, duedate, completed = row # assign row(aka item) into title, duedate, completed
                                                # Each line in the file holds one task as title,due_date,completed
                        if duedate == "": # says "if no info is provided by user or source an dis left empty, then... "
                            duedate = None # ...then assign the value 'None' to 'duedate'

                        task = add_task(task_list, title, duedate) # It rebuilds the Task (and parses the date).
                                                       # IOWs, it calls your add_task function to build one task from the values 
                                                       # read off a row of the 'file'.
                                                       # and then stores the result in a variable named 'task'. IOWs:
                                                       # 1) 'add_task(task_list, title, duedate)' runs. If there is a 'due date', it
                                                       # converts the 'due date' string into a 'datetime.date', then creates a Task 
                                                       # OBJECT, and appends it to task_list.
                                                       # 2) 'task' = it stores what 'add_task' returns, 
                                                       # by calling 'add_task(task_list, title, duedate)' from here. Your 'add_task' function below
                                                       # ends with "return 'new_task'", so 'task' variable here now refers to the same 
                                                       # task object that was just added to the list.
                                                       # PS, the 'new_task' task below is the variable that this 'add_task' function dumps into.
                                                       # The 'add_task' function is a different function in this same file (todolist.py)
                        task.completed = (completed == 'True') # 'completed' = parameter imported from 'task.py'. CORRECTION: 'completed'
                                                       # here is a text string ("True" or "False") read from the 'file' row, NOT something
                                                       # that is imported from 'task.py'. The line converts that text into a real boolean.
                                                       # (completed == 'True') that parameter is made to be True here, to
                                                       # indicate the task is completed.
                                                       # Once the parameter is evaluated to True, it gets assigned to 'task.completed',
                                                       # is is an assignment to '.completed', that then gets added to the 'task' at hand
                                                       # which consequently gets marked '[X]'.
                                                       # Otherwise, for a row ending in 'False', the comparison gives 'False', so the task stays '[-]'.

        ########################## Protect the actual file-reading operation:
        except FileNotFoundError: 
            print("No saved tasks file found. Starting with an empty list.") 
            return []

        except PermissionError:
            print("Error: Permission denied when trying to load tasks.")
            return []

        except OSError as e:
            print(f"Error loading tasks: {e}")
            return []
        
    return task_list  # the 'load_tasks' function hands back the finished list to be used elsewhere.

# This block addresses bug - "A: empty title (just Enter)"
def add_task(task_list, title, due_date=None):
    if not title.strip():
        print("\nError: task title cannot be empty.")
        return None

    if isinstance(due_date, str): # says "if due date input is of string data type... "
        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date() # "...then convert 'string due_date' to 'date due_date'"
        except ValueError: # catches the error when Python cannot convert the date string into a valid date.
            print(f"Error: '{due_date}' is not a valid date. Use YYYY-MM-DD.") # displays a helpful message to the user.
            return None # stops the function when the date is invalid and signal that no task was created successfully.
                        # in other words, immediately exits the 'add_task()' function without creating or adding a task.
    new_task = Task(title, due_date) # then using the 'Task()' class imported from 'task.py' script, create a new task 'new_task'...
    task_list.append(new_task) # ...and add such task to the list defined in the 'add_task()' function.
    # print(add_task(task_list)) # this would cause infinite recursion if you ever uncommented it, since the function would call 
                                # itself. It’s safe as a comment.
    print(f"\nTask '{title}' added.") # this string message appears in order to confirm addition of task, each time to add a task
    return new_task # return the contents of 'new_task' variable


############################### Marks the task at the given index as completed. ########################################

def complete_task(task_list, index):
    try: # A) Exception handling for bad index ONLY, it does not raise anything for invalid characters and crashes
        if index < 0:  # part a) This adresses the bug caused by '-1' for completed tasks. "11) C: negative index (-1)"
            raise IndexError # part b) This adresses the bug caused by '-1'  for completed tasks. "11) C: negative index (-1)". 
                             # VIP Note: notice how this line calls the except error message I put together myself in 'except 
                             # IndexError:' below. 
        task = task_list[index]   # 1) grab the task at that position
        # task_completed = task.completed 
        task.completed = True  # 2) mark it as completed
        print(f"\nTask '{task.title}' marked as completed.") # line confirms that a certain task was completed
        return task # Option 2a:  [X] Task: Testing adding a task (due 2026-11-20)
    except IndexError: # B) Exception handling for bad index ONLY, it does not raise anything for invalid characters and crashes
        print(f"\nError: there is no task number {index}.") # C) Exception handling for bad index ONLY, it does not raise anything for invalid characters and crashes
        return None # D) Exception handling for bad index ONLY, it does not raise anything for invalid characters and crashes

########################################## Removes the task at the given index. ###############################################

def delete_task(task_list, index):
    try: # A) Exception handling for bad index ONLY, it does not raise anything for invalid characters and crashes.
        if index < 0: #  # part a) This adresses the bug caused by '-1' for deleted tasks. "11) C: negative index (-1)"
            raise IndexError # part b) This adresses the bug caused by '-1'  for deleted tasks. "11) C: negative index (-1)". 
                             # VIP Note: notice how this line calls the except error message I put together myself in 'except 
                             # IndexError:' below. 
        task = task_list[index]
        # task_list.pop(task) # '.pop()' method works on numbers ONLY, NOT strings, so using the str 'task' will cause the exception:
                            # 'TypeError: 'Task' object cannot be interpreted as an integer'
        task_list.pop(index) # so Python gives you the option to refer to that same task, by number as well, iows, by its index.
        print(f"\nTask '{task.title}' deleted.")  # this string message appears in order to confirm deletion of task, each time to delete a task
        return(task)
    except IndexError: # B) Exception handling for bad index ONLY, it does not raise anything for invalid characters and crashes.
        print(f"Error: there is no task number {index}.") # C) Exception handling for bad index ONLY, it does not raise anything for invalid characters and crashes.
        return None # D) Exception handling for bad index ONLY, it does not raise anything for invalid characters and crashes

########################################## Returns or prints a formatted list of tasks ###############################################
''' 
- list_tasks(task_list): Returns or prints a formatted list of tasks showing index, status, title, and due date. Indicate if 
a task is overdue by comparing the due date with today's date.
'''

def list_tasks(task_list):
    if not task_list: # a) ensures that the user gets informed with message "No tasks found." when you enter an index number for 
                      # an empty file when user either C or D.
        print("No tasks found.") # b) ensures that the user gets informed with message "No tasks found." when you enter an index
                                # number for an empty file when user either C or D.
        return  # c) ensures that the user gets informed with message "No tasks found." when you enter an index number for an 
                # empty file when user either C or D.
    for index, task in enumerate(task_list): # Interesting, usually when you run through a loop, you do so for one item (ex, 'i'),
                                            # in this case however, you're doing it for 2 items ('index', 'task'), 'task' being
                                            # the declared variable to which 'task_list[index]' was assigned to.
                                            # 'enumerate()' gives you the 'position' and the 'task' together, avoiding having 
                                            # to count the indexes yourself
        # print(dir(datetime))
        # print(dir(date))
        overdue = ""
        # if task.due_date < date.today():
        if task.due_date is not None and task.due_date < date.today(): # This says "If today's date is greater/surpassed
                                                                       # 'task.due_date', it means 'task.due_date' is "OVERDUE"
                                                                       # if this calculation is not properly set up, tasks will
                                                                       # be marked "OVERDUE" incorrectly.
                                                                       # Also without "task.due_date is not None", the script
                                                                       # will crash with "TypeError: '<' not supported between
                                                                       # instances of 'NoneType' and 'datetime.date'"as soon as 
                                                                       # it encounters a task that has no due date, bc 'task.due_date'
                                                                       # can not compare to 'None' values                                                 
            overdue = "OVERDUE"

        # print(f"{index}: {task}") 
        print(f"{index}: {task} {overdue}")


# Test for code above:
if __name__ == "__main__":
    task_list = []
    add_task(task_list, "Past due task", "2020-01-01")   # overdue
    add_task(task_list, "Future task", "2026-11-20")     # not overdue
    add_task(task_list, "Task with no date")             # no due date

    complete_task(task_list, 1)                          # mark the future task done

    list_tasks(task_list)




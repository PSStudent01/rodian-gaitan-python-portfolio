'''
Task 3: Develop the User Interface

    Create a main script (e.g., main.py) that:
        Presents a text-based menu with the options:
            (A) Add a new task.
            (C) Mark a task as completed.
            (D) Delete a task.
            (L) List all tasks.
            (Q) Quit.
        Implements the menu loop so that after each operation the menu is shown again until the user chooses to quit.
        For each menu option, prompts the user for necessary input and calls the corresponding function from todolist.py.
        Before quitting, prompts the user to save the current task list to a file.
'''

# from task import Task
from todolist import add_task, complete_task, delete_task, list_tasks # importing all functions from 'todolist.py' file
from todolist import load_tasks  # % 1) importing task 'load_task'. This is done at the very end as part of connecting to 
                                 # the "file loading process".
from todolist import save_tasks # [ PART 2a, look at PART 1 in 'todolist.py']

def main(): # defining the 'main()' function.
    # task_list = [] # created list container inside 'main()' (or before it), so the same list is passed to every call.
    task_list = load_tasks() # % 2) Replace the above line. This is done at the very end as part of connecting to the "file loading process"
    selection = "" # Since we're working w/ 'while loop', this is starting point. Similar to count = 0 for a 'while' loop.
    # while selection != "q": # says "for as long as the selection made is not 'q' run the following action, see below:"
    while selection not in ("q", "Q"): # says "for as long as the selection made is not 'q' or 'Q', run the following action, 
                                       # see below, which is essentially... 
                                       # a) the persisting 'Main Menu'
                                       # b) prompting user for a 'Main Menu' option, which eventually may turn prompts user for 
                                       # sub-menu options."
        print("""\n==================== Task Manager ==========================: 
            (A) Add a new task.
            (C) Mark a task as completed.
            (D) Delete a task.
            (L) List all tasks. 
            (Q) Quit.
            """)
        selection = input("Select menu option: ") # Selection input function for Main Menu. BTW, without it'll get caught in loop

        # Menu selection to add a task:
        # if selection == 'a' or selection == 'A':
        if selection in ('a', 'A'): # a more simplified approach to the above line
            # pass
            # add_task() # this would never work here!
            title = input("Enter task title: ") # this captures user input specific to adding the task title and stores it in 
                                                # variable 'title' for later manipulation of its contents.
            duedate = input("Enter task due date: ") # this captures user input specific to adding the task due date and stores 
                                                     # it in variable 'duedate' for further manipulation of its contents.
            if duedate == "": # conditional branch says that if no input is entered for 'due date' by the user...
                duedate = None # ...the value None is be reassigned to variable 'duedate'.
            add_task(task_list, title, duedate) # Interesting, here we're calling the function 'add_task(task_list, title, duedate)'
                                                # with all 3 arguments that we need, by importing such function from the 
                                                # 'todolist' script, rather than having the function in this same file and calling it
                                                # from here.

        # Menu selection to mark a task completed:
        # elif selection == 'c' or selection == 'C':
        elif selection in ('c', 'C'): # a more simplified approach to the above line
            # pass
            # complete_task() # this would never work here!
            # title = input("Enter task title: ")
            # duedate = input("Enter task due date: ")
            list_tasks(task_list) # here we momentarily extract/pull the 'task_list' by calling its fuction 
                                    # 'list_tasks(task_list)' to manipulate one of its items (itc, mark task(0) as completed!).
                                    # you can place it further to the bottom as seen below and it'll still work.
            try: # A) Exception handling for invalid characters and crashes ONLY, NOT for bad index.
                index = int(input("Number of the task to mark completed: ")) # this captures user input identifying which task INDEX
                                                                         # is to be marked completed & store it in variable 'index' 
                                                                         # for further manipulation of its contents, like 
                                                                         # identifying the item to be marked completed.
                #list_tasks(task_list) # see comments 2 line above.
                complete_task(task_list, index) # Interesting, here we're calling the function 'complete_task(task_list, index)'
                                            # with all 2 arguments that we need, by importing such function from the 
                                            # 'todolist' script, rather than having the function in this same file and calling it
                                            # from here.
            except ValueError:  # B) Exception handling for invalid characters and crashes ONLY, NOT for bad index.
                print("\nError: please enter a number, like 0 or 1.")  # C) Exception handling for invalid characters and crashes ONLY, NOT for bad index.

        # Menu selection to delete a particular task:
        # elif selection == 'd' or selection == 'D':
        elif selection in ('d', 'D'): # a more simplified approach to the above line
            # pass
            # delete_task() # this would never work here!
            list_tasks(task_list) # here we momentarily extract/pull the 'task_list' by calling its fuction 
                                  # 'list_tasks(task_list)' to manipulate one of its items (itc, delete task(0)).
                                  # you can place it further to the bottom as seen below and it'll still work.
            try: # A) Exception handling for invalid characters and crashes ONLY, NOT for bad index.
                index = int(input("Number of the task to be deleted: ")) # this captures user input identifying which task INDEX
                                                                     # is to be deleted & store it in variable 'index' 
                                                                    # for further manipulation of its contents, like identifying
                                                                    # the item to be deleted.
                # list_tasks(task_list) # see comments 2 line above.
                # task_list.pop(index)
                delete_task(task_list, index) # Interesting, here we're calling the function 'delete_task(task_list, index)'
                                          # with all 2 arguments that we need, by importing such function from the 
                                          # 'todolist' script, rather than having the function in this same file and calling it
                                          # from here.
            except ValueError: # B) Exception handling for invalid characters and crashes ONLY, NOT for bad index.
                print("\nError: please enter a number, like 0 or 1.") # C) Exception handling for invalid characters and crashes ONLY, NOT for bad index.

        # Menu selection to list all existing tasks:
        # elif selection == 'l' or selection == 'L':
        elif selection in ('l', 'L'): # a more simplified approach to the above line
            # pass
            # list_tasks() # this would never work here!
            list_tasks(task_list) # here we momentarily extract/pull the 'task_list' by calling its function 
                                  # 'list_tasks(task_list)' to manipulate one of its items (itc, simply VIEW the entire list).

        # Menu selection to quit out of the script/app:
        # elif selection == 'q' or selection == 'Q':
        elif selection in ('q', 'Q'): # a more simplified approach to the above line
            # pass
            # print("Please save the current task to a file! \n")
            # exit_app() # this would never work here!
            save = input("Save tasks before quitting? (Y/N): ").lower()# this captures user input identifying whether yes or no
                                                                     # to saving the list of tasks and then storing the answer in
                                                                     # variable 'save' for further manipulation of its contents, like identifying
                                                                    # the for the answer to be processed by the next nested
                                                                    # logical branch.
            if save == 'y':
                # print("Saving...") # [ PART 2b, look at PART 1 in 'todolist.py']. Here we replace this placeholder with 
                                     # code blcok below:
                save_tasks(task_list) # [ PART 2c, look at PART 1 in 'todolist.py']. is a 'function call'. It runs the 'save_tasks'
                                      # function you wrote in 'todolist.py' and hands it the current list of tasks to write to the file.
                print("Tasks saved!")
            print("Good Bye! \n") # 2)... move to here, so that now The spec just says to prompt before quitting, and either 
                                  # answer should end the program cleanly.
            #else:
                #print("Good Bye! \n") # 1) The goodbye only prints when the user answers anything other than y. Your if/else puts 
                                       # print("Good Bye!") in the else, so if the user types y, it prints “Saving...” and then 
                                       # never says goodbye. The spec just says to prompt before quitting, and either answer 
                                       # should end the program cleanly.
                                       # Fix: Moving the 'goodbye' out of this 'else' bracnh into the 'elif' branch above...

        # Default message if no valid entry made:
        else:
            print("Enter a valid option!")
        
main() # calls the function 'main()' to action.






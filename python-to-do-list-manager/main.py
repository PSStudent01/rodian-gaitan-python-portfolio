'''
Main script for the Personal To-Do List Manager.
Displays the menu and handles user input by calling functions from todolist.py.
'''

from todolist import add_task, complete_task, delete_task, list_tasks
from todolist import load_tasks
from todolist import save_tasks


def main():  # Defines the main() function.

    # Loads previously saved tasks into the task_list.
    task_list = load_tasks() 

    # Initializes selection so the while loop can begin.
    selection = "" 

    # Continues displaying the menu until the user selects Q or q.
    while selection not in ("q", "Q"):

        print("""\n==================== Task Manager ==========================: 
            (A) Add a new task.
            (C) Mark a task as completed.
            (D) Delete a task.
            (L) List all tasks. 
            (Q) Quit.
            """)

        # Captures the user's main menu selection.
        selection = input("Select menu option: ")

        # Menu selection to add a task:
        if selection in ('a', 'A'):
            title = input("Enter task title: ")
            duedate = input("Enter task due date: ")

            # Assigns 'None' when the user leaves the optional due date blank.
            if duedate == "":
                duedate = None

            # Passes the task list, title, and due date to add_task().
            add_task(task_list, title, duedate)

        # Menu selection to mark a task completed:
        elif selection in ('c', 'C'):

            # Displays the current tasks so the user can identify the task index.
            list_tasks(task_list)

            try:
                # Captures the task index and converts the input string to an integer.
                index = int(input("Number of the task to mark completed: "))

                # Passes the task list and selected index to complete_task().
                complete_task(task_list, index)

            # Handles input that cannot be converted to an integer.
            except ValueError:
                print("\nError: please enter a number, like 0 or 1.")

        # Menu selection to delete a particular task:
        elif selection in ('d', 'D'):

            # Displays the current tasks so the user can identify the task index.
            list_tasks(task_list)

            try:
                # Captures the task index and converts the input string to an integer.
                index = int(input("Number of the task to be deleted: "))

                # Passes the task list and selected index to delete_task().
                delete_task(task_list, index)

            # Handles input that cannot be converted to an integer.
            except ValueError:
                print("\nError: please enter a number, like 0 or 1.")

        # Menu selection to list all existing tasks:
        elif selection in ('l', 'L'):

            # Displays all tasks in the current task list.
            list_tasks(task_list)

        # Menu selection to quit the application:
        elif selection in ('q', 'Q'):

            # Asks the user whether to save the current task list before quitting.
            save = input("Save tasks before quitting? (Y/N): ").lower()

            if save == 'y':

                # Passes the current task list to save_tasks() to write it to the CSV file.
                save_tasks(task_list)
                print("Tasks saved!")

            # Displays the goodbye message regardless of the save response.
            print("Good Bye! \n")

        # Displays an error message if the user enters an invalid menu option.
        else:
            print("Enter a valid option!")


# Calls main() to start the application.
main()

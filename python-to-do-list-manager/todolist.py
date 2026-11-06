''' 
To-do list manager functions.
Functions for adding, completing, deleting and listing Task objects, plus saving and loading the list as a CSV file. Used by 
main.py.
'''

from task import Task
from datetime import datetime, date
import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # A) Grabs the directory containing this todolist.py file.
                                                      # Prevents user from manually having to cd to the project
                                                      # root folder in order to run program


def save_tasks(task_list, filename="tasks.csv"):
    filename = os.path.join(BASE_DIR, filename)  # B) Build the full path to tasks.csv.
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for task in task_list:
                # Write each task's title, due date, and completion status as one CSV row.
                # Use an empty string when no due date is provided instead of writing None.
                writer.writerow([task.title, task.due_date or "", task.completed])
    except OSError as e:
        print(f"Error: could not save tasks ({e}).")


def load_tasks(filename="tasks.csv"):
    filename = os.path.join(BASE_DIR, filename)  # C) Build the full path to tasks.csv.
    task_list = []
    if os.path.exists(filename):
        try:
            with open(filename, "r", newline="") as file:
                for row in csv.reader(file):
                    # Skip rows that do not contain the three expected task values.
                    if len(row) != 3:
                        continue

                    title, duedate, completed = row

                    # Convert an empty due-date field back to None.
                    if duedate == "":
                        duedate = None

                    # Re-create the Task object and add it to task_list.
                    task = add_task(task_list, title, duedate)

                    # Convert the CSV text value ("True" or "False") to a Boolean.
                    task.completed = (completed == 'True')

        except FileNotFoundError:
            print("No saved tasks file found. Starting with an empty list.")
            return []

        except PermissionError:
            print("Error: Permission denied when trying to load tasks.")
            return []

        except OSError as e:
            print(f"Error loading tasks: {e}")
            return []

    return task_list


def add_task(task_list, title, due_date=None):
    if not title.strip():
        print("\nError: task title cannot be empty.")
        return None

    if isinstance(due_date, str):
        try:
            # Convert a date string into a datetime.date object.
            due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            print(f"Error: '{due_date}' is not a valid date. Use YYYY-MM-DD.")
            return None

    new_task = Task(title, due_date)
    task_list.append(new_task)
    print(f"\nTask '{title}' added.")
    return new_task


def complete_task(task_list, index):
    try:
        # Reject negative indexes so they cannot select tasks from the end of the list.
        if index < 0:
            raise IndexError

        task = task_list[index]
        task.completed = True
        print(f"\nTask '{task.title}' marked as completed.")
        return task
    except IndexError:
        print(f"\nError: there is no task number {index}.")
        return None


def delete_task(task_list, index):
    try:
        # Reject negative indexes so they cannot delete tasks from the end of the list.
        if index < 0:
            raise IndexError

        task = task_list[index]
        task_list.pop(index)
        print(f"\nTask '{task.title}' deleted.")
        return(task)
    except IndexError:
        print(f"Error: there is no task number {index}.")
        return None


def list_tasks(task_list):
    if not task_list:
        print("No tasks found.")
        return

    for index, task in enumerate(task_list):
        overdue = ""

        # Check that a due date exists before comparing it with today's date.
        if task.due_date is not None and task.due_date < date.today():
            overdue = "OVERDUE"

        print(f"{index}: {task} {overdue}")


# Run these test examples only when todolist.py is executed directly.
if __name__ == "__main__":
    task_list = []
    add_task(task_list, "Past due task", "2020-01-01")   # overdue
    add_task(task_list, "Future task", "2026-11-20")     # not overdue
    add_task(task_list, "Task with no date")             # no due date

    complete_task(task_list, 1)                          # mark the future task done

    list_tasks(task_list)

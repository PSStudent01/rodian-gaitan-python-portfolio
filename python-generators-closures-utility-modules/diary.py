'''
Diary program.
Creates diary.txt if it doesn't exist, appends a timestamped entry, and prints every entry. Each file operation has its own 
try/except so the message shows which step failed.
'''

# Using try/except blocks to catch and report errors during file operations:
# The idea is to wrap each file operation in its own try/except so the error message tells you which step failed.
import os
import datetime

# FILENAME = "nonexistent_folder/diary.txt" # line to test Error handling for bad path. The file or even the file path in an 
                                            # Absolute or Relative file path is incorrect or that the specified directory 
                                            # or path doesn't exist. In other words, keep in mind that catching an exception 
                                            # doesn't automatically stop the rest of the program. In other words, is not
                                            # necessarily that ile itself cannot be found. When opening in append mode, a 
                                            # missing file is created. The missing parent directory is what causes 
                                            # FileNotFoundError in this situation.
FILENAME = "diary.txt" # allows us to modify the file name or even directory path from this location, across the entire script
                       # wherever the 'FILENAME' variable is plugged in.

# Step 1: Create the file if it doesn't exist
try:  # <----------------------------------{1) exception handler try/except block starts}
    if os.path.exists(FILENAME):
        print(f"'{FILENAME}' exists in the current directory.")
    else:
        with open(FILENAME, "a"):
            pass # means there is no additional operation inside the with block.
        print(f"'{FILENAME}' did not exist, so a new one has been created.\n")
except FileNotFoundError: # <----{4a) exception handler is triggered (instead of traceback 'FileNotFoundError' if the file or even
                          # the file path in an Absolute or Relative file path is incorrect or that the specified directory 
                          # or path doesn't exist,)}. Initially placed after 'OSError', causing a potential bug.
                          # IOWs, it handles cases where the specified directory or file path cannot be found, such as 
                          # when a parent directory doesn't exist.
    print(f"Error: '{FILENAME}' could not be found.")  # <---{4b) message replacing the default traceback message for the 
                                                           # exception 'FileNotFoundError'.}
except PermissionError: # <----{2a) exception handler is triggered (instead of traceback 'PermissionError' if user lacks 
                                # needed permissions to access the file.)}
    print(f"Error: no permission to create '{FILENAME}'.") # <---{2b) message replacing the default traceback message for the 
                                                           # exception 'PermissionError'.}
except OSError as e: #  <-----{3a) exception handler is triggered (instead of traceback 'OSError' if operating-system-related 
                                # errors occur)}
                                # IOWs, # Handles other operating-system-related file errors that aren't caught by the more 
                                # specific exception handlers above.
    print(f"Error while checking/creating the file: {e}") # <---{3b) message replacing the default traceback message for the 
                                                           # exception 'OSError'.}

# Step 2: Get the entry and build the timestamp
entry = input("Enter diary entry: ")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Step 3: Append the entry
try: # <----------------------------------{1) exception handler try/except block starts}
    with open(FILENAME, "a") as file:
        file.write(f"- {timestamp}: {entry}\n")
except FileNotFoundError: # <----{4a) exception handler is triggered (instead of traceback 'FileNotFoundError') if the file or even
                                # the file path in an Absolute or Relative file path is incorrect.}
                                # IOWs, it handles cases where the specified directory or file path cannot be found, such as 
                                # when a parent directory doesn't exist.
    print(f"Error: '{FILENAME}' could not be found.")  # <---{4b) message replacing the default traceback message for the 
                                                           # exception 'FileNotFoundError'.}
                                                            # Initially placed after 'OSError', causing a potential bug.
except PermissionError: # <-----{2a) exception handler is triggered (instead of traceback 'PermissionError' if user lacks needed
                                # permissions to access the file. )}
    print(f"Error: no permission to write to '{FILENAME}'.")  # <---{2b) message replacing the default traceback message for 
                                                              #the exception 'PermissionError'.}
except OSError as e: #  <-----{3a) exception handler is triggered (instead of traceback 'OSError' if operating-system-related 
                                # errors occur)}
                                # IOWs, it handles other operating-system-related file errors that aren't caught by the more 
                                # specific exception handlers above.
    print(f"Error while writing to the file: {e}") # <---{3b) message replacing the default traceback message for the exception 
                                                   # 'OSError'.}

# Step 4: Read and display all entries
try:  # <----------------------------------{1) exception handler try/except block starts}
    with open(FILENAME, "r") as file:
        contents = file.read()
    print("#======== Diary Entries =======#")
    print(contents)
except FileNotFoundError: # <----{2a) exception handler is triggered (instead of traceback 'FileNotFoundError' if the file or even
                                # the file path in an Absolute or Relative file path is incorrect )
                                # IOWs, it handles cases where the specified directory or file path cannot be found, such as 
                                # when a parent directory doesn't exist.}
                                # Initially placed here, which was the correct place to begin with.
    print(f"Error: '{FILENAME}' could not be found.")  # <---{2b) message replacing the default traceback message for the 
                                                           # exception 'FileNotFoundError'.}
except PermissionError: # <-----{3a) exception handler is triggered (instead of traceback 'PermissionError' if user lacks needed 
                                # permissions to access the file. )}
    print(f"Error: no permission to read '{FILENAME}'.") # <---{3b) message replacing the default traceback message for the 
                                                           # exception 'PermissionError'.}
except OSError as e:  # <-----{4a) exception handler is triggered (instead of traceback 'OSError' if operating-system-related 
                                # errors occur)}
                                # IOWs, it handles other operating-system-related file errors that aren't caught by the more 
                                # specific exception handlers above.
    print(f"Error while reading the file: {e}")  # <---{4b) message replacing the default traceback message for the exception 
                                                   # 'OSError'.}





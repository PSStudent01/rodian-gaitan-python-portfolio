'''
List manager:
A text menu for managing a list of integers: add a number, remove one by index, display the list, or quit. try/except keeps 
the program running when the user enters a non-integer or an invalid index.
'''

numbers = [12, 45, 7, 89, 23, 56, 3, 71, 34]

def add_num():
    # Prompts for an integer and appends it to the list:
    try: # 1) Exception Handling: if the following code throws an error (itc, a 'ValueError') due to invalid data input....
        integer = int(input("Enter an integer: ")) # a) it takes in input from user and casts it as interger type and stores it.
        numbers.append(integer) # b) then takes that user casted user input form 'interger' and appends it to the 'numbers' list.
        print(f"Added: {integer}") # c) then it prints the interger that was appended to the list.
    except ValueError: # 2) Exception Handling:...it replaces the ValueError long Traceback message with the following message below, so that the 
                       # script won't crash:
        print("Invalid input: please enter a whole number.")

def subtract_num():
    # Prompts for an index and removes the item at that position:
    try: # 1) Exception Handling: if the following code throws an error (itc, a 'IndexError' or 'ValueError')
        index = int(input("Enter the index to remove: ")) # Prompts the user for an index; it casts it to interger type; stores 
                                                          # it in 'index' variable.
        removed = numbers.pop(index) # it removes the interger value in the 'numbers' list linked to the index entered by the user.
                                     # and stores it in variable 'removed'.
        print("Removed: ", removed) # then it prints the interger removed from the list
    except IndexError: # 2a) Exception Handling:...it replaces the 'IndexError' long Traceback message with the following message 
                       # below, so that the script won't crash:
        print("Invalid index: please enter a valid index.")
    except ValueError: # 2b) Exception Handling:...it replaces the 'ValueError' long Traceback message with the following message
                       # below, so that the script won't crash:
        print("Invalid input: please enter a whole number.")

def display_list():
    print(numbers) # Prints the current 'numbers' list.

def main():
    selection = "" # empty starting point for 'selection' 
    while selection != 'd': # as long as value for 'selection' is not 'd', it prints the menu below:
        print("""\nIntegers menu: 
            (a) Add a number
            (b) Remove a number 
            (c) Display the list 
            (d) Quit
            """)
        
        selection = input("Select a menu option: ").lower() # It takes user input as upper or lower case and stores it 
                                                            # in 'selection' variable.

        if selection == 'a': # if user input is 'a', it calls the function below...
            add_num()
        elif selection == 'b': # if user input is 'b', it calls the function below...
            subtract_num()
        elif selection == 'c': # if user input is 'c', it calls the function below...
            display_list()
        elif selection == 'd': # if user input is 'd', it stops displaying menu and instead prints message below...
            print("Good-Bye! \n") 
        else:  # if anything other than the available menu options is entered, the message below is printed
            print("Enter a valid option!")  

if __name__ == "__main__":            
    main()


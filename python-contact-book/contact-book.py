
# ===================================== CONTACT BOOK APPLICATION  ================================================== #
"""Contact book.
A command-line contact book built with functions and a dictionary (name -> phone number). A menu loop lets the user 
add a contact (with input validation), view all contacts, search by full or partial name (not case-sensitive), delete 
a contact, or exit. Contacts are stored in memory only, so they are lost when the program ends.
"""
# MENU
# Defining a function to display the menu:

def show_menu():
    print("\nContact Book Menu:") # displays menu option
    print("1) Add New Contact")  #     ""     ""    ""
    print("2) View All Contacts")  #    ""     ""    ""
    print("3) Search Contact")    #     ""     ""    ""
    print("4) Delete Contact")  #     ""     ""    ""
    print("5) Exit")            #     ""     ""    ""
# print(show_menu()) # Testing. Renders the whole menu. 

# 1) ADDING CONTACT
# 1A) # Defining add_contact() to...
## validate input
## store a new contact
# This function's job is to ask for a name and phone number, then add them to contacts.
def add_contact(contacts): # defining the function
    name = input("Enter name: ").strip() # takes in string input from a user, while removing any whitespaces from the string.

    # Conditional branch chain used to validate input data stored in 'name' from 'input().strip()'
    if name == "": # if no data entered....
        print("Name cannot be empty.") # this is the message that renders as output when return executes
        return # returns when function "add_contact(contacts)" is called and conditional branch "if name == ''" is True

    if name in contacts: # if key data entered is already stored in dictionary....
        print("That name already exists. Contact not added.")  # this is the message that renders as output when return executes
        return # returns when function "add_contact(contacts)" is called and conditional branch " if name in contacts:" is True
               # [return is used to bail out early when something is wrong, so the code below doesn’t run.]
    # Conditional branch chain used to validate input data stored in 'phone' from 'input().strip()'
    phone = input("Enter phone number (digits only): ").strip()  # takes in string input from a user, while removing 
                                                                 # any whitespaces from the string.
    if not phone.isdigit() or len(phone) < 7 or len(phone) > 15: # if the entry is NOT all digits OR is shorter than 7
                                                                 # or longer than 15 characters...
        print("Invalid phone number. Use 7 to 15 digits only.") # this is the message that renders as output when return executes
        return # returns when function "add_contact(contacts)" is called and conditional branch 
               # "if not phone.isdigit() or len(phone) < 7 or len(phone) > 15:" is True.
               # [return is used to bail out early when something is wrong, so the code below doesn’t run.]

    contacts[name] = phone # If we got past every check, this stores the 'contact' key name, and 'phone' value.
    print("Contact added.") # and consequently the confirmation message is displayed


# 2) VIEWING CONTACTS
# 2A) # Defining view_contacts() to display every stored contact.
def view_contacts(contacts): # defining the function
    if len(contacts) == 0: # validating for existence of at least 1 contact, as no point in moving forward if there is none.
        print("Your contacts list is currently empty! Please add at least 1 contact") # if the condition above is True, this is
                                                                                      # the message that renders as output.
    else: 
        for contact in contacts:  # it loops through the 'contacts' dictionary and for each contact.....
            print(f"{contact}: {contacts[contact]}") #...it prints the contact key (name) and the contact value (phone #)


# 3) SEARCHING CONTACTS
# 3A) # Defining 'search_contact()' to find contacts by full or partial name (not case-sensitive)
def search_contact(contacts): # defining the function
    search = input("Enter a name to search: ").strip().lower() # takes in string input from a user, removes any surrounding whitespace, 
                                                               # and lowercases it so that the search is not case-sensitive.
    found = False # is a flag as a variable that remembers whether anything matched. Starting assuming nothing did.

    for name in contacts:  # it loops through the 'contacts' dictionary and for each name.....
        if search in name.lower(): # ...if the text entered by the user appears anywhere in the 'name' key (partial match, any case)
            print(f"{name}: {contacts[name]}") # ...it prints the contact key (name) and the contact value (phone #)
            found = True # this flips the flag whenever a match is printed. There’s no break because we want to check every contact.

    if not found: # sits at the same indentation as the 'for', so it runs once, after the loop finishes.
        print("No matching contact found.") # this is the message that renders as output if no matches are found


# 4) DELETING CONTACTS
# Defining 'delete_contact()' to remove a contact by name
def delete_contact(contacts):  # defining the function
    name = input("Enter name to be removed: ").strip() # takes in string input from a user, while removing any whitespaces from the string.
    if name in contacts: # if the name entered by the user, matches the 'name' key in the 'contacts' dictionary...
        contacts.pop(name) #...removes the contact (name and phone number) from the dictionary
        # del contacts[name] # as an alternative...also deletes the entire contact from the dictionary
        print(f"{name} has been removed")  # this is the message that renders as output to confirm that the contact has been removed
    else: # otherwise, if the name to be deleted does not exist...
        print("That contact does not exist.") # this is the message that renders as output if no match is found


# 1B) Defining a main loop program to run the program and keep the contacts dictionary in one place. 
def main(): # 'main()' function. It represents the whole app
    contacts = {} # starting with an empty dictionary

    while True: # 'while True' keeps the loop running until the user selects 5, which runs 'break' and ends it.
                # On every pass through the loop, it does as follows:
        show_menu() # call the function, which prints the menu because the function has several 'print()' calls
                    # in it. Also, because it’s inside the loop, it prints again after every action.
        selection = input("Enter your choice (1-5): \n") # take input from the user and stores it inside the 'selection' variable for its
                                                       # value to be used anywhere else in the program.
        # Self-explanatory conditional branch chain:
        if selection == "1": # 1B)CALL TO 'add_contact(contacts)'so that if selection 1 pressed...
            add_contact(contacts) # ...call to function is executed, which allows you to add contacts to the dictionary
        elif selection == "2": # 2B)CALL TO 'view_contacts(contacts)'so that if selection 2 pressed...
            view_contacts(contacts) #...call to function is executed, which allows you to view all contacts from the dictionary
        elif selection == "3": # 3B)CALL TO 'search_contact(contacts)'so that if selection 3 pressed...
            search_contact(contacts) #...call to function is executed, which allows you to search contacts for a full/partial name
        elif selection == "4":  # 4B)CALL TO 'delete_contact(contacts)'so that if selection 4 pressed...
            delete_contact(contacts) #...call to function is executed, which allows you to delete the name of interest
        elif selection == "5": # 5A) Otherwise, if user selects option 5....
            print("Goodbye!") # this is the message that renders as output,
            break # breaks out of the 'while' loop to prevent it from looping endlessly, since there is no increment/de-crement counter
                  # to count towards an end
        else:
            print("Invalid choice. Please enter a number from 1 to 5.") # if all of the above elif conditions return 'False',
                                                                        # the 'else' statement is executed as a final alternative

main() # calls the 'main' function to run all of its actions within it

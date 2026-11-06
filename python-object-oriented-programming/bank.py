'''
Bank Account Management - Base Class

Demonstrates object-oriented programming (OOP) concepts by defining a BankAccount class with account attributes, deposit and 
withdrawal methods, input validation, and exception handling.

Includes a string representation of the account and test code demonstrating successful transactions, invalid amounts, and
insufficient funds.
'''

class BankAccount:
    # Defines initializer / constructor:
    # This method initializes the attributes when a new BankAccount object is created.
    def __init__(self, account_number, owner, balance=0): # Defining initializer with dunder '__init__' (aka 'dunder init method')
        # Initializes the account's attributes:
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    # Defines methods:
    def deposit(self, amount):
        if amount <= 0: # Conditional checks whether the amount to be deposited is <= 0. If True, it raises the exception below....
            raise ValueError("Invalid amount. Enter a deposit amount greater than $0.00.") 
        self.balance += amount # Otherwise, adds the deposit amount to the account's balance.
        print(f"Amount deposited: ${amount:.2f}") # Displays the amount deposited with two decimal places.
        print((f"New balance: ${self.balance:.2f}")) # Displays the balance with two decimal places.
        return self.balance # Returns the updated account balance to the caller.

    def withdraw(self, amount):
        # 1) Validate the withdrawal amount FIRST.
        if amount <= 0:  # WITHOUT this conditional branch guard, It doesn’t reject non-positive amounts and account.withdraw(-100) 
                         # would pass the self.balance < amount check (500 < -100 is false), and then self.balance - (-100) 
                         # would add $100 to the account, rather than deducting.
            raise ValueError("Invalid amount. Enter a withdrawal amount greater than $0.00.") 
        
        # 2) Check whether sufficient funds are available BEFORE processing the withdrawal.
        if self.balance < amount: # If self.balance < amount evaluates to True, the withdrawal amount exceeds the
                                  # current account balance, so a ValueError exception is raised.
                                  # Otherwise, execution continues and the withdrawal amount is deducted from the balance.
            raise ValueError("Insufficient funds: cannot withdraw more than the current balance.")  
        self.balance = self.balance - amount # Subtracts the withdrawal amount from the account's balance.
        print(f"Amount withdrawn: ${amount:.2f}") # Displays the withdrawn amount with two decimal places.
        print((f"New balance: ${self.balance:.2f}")) # Displays the updated balance with two decimal places.
        return self.balance # Returns the updated account balance to the caller.

    def __str__(self):
        # Returns a readable string representation of the account.
        return f"Account {self.account_number} - Owner: {self.owner}, Balance: ${self.balance:.2f}" # 2a) Displays customer's profile by default.


def main(): 
    # Creating an instance of BankAccount:
    account = BankAccount(12345, "Alice", 500) # 2c) Eventhough you later defined a '__str__' method above, this line
                                               # is still necessary because this is where the object is being created.
                                               # and initialized. Also, this is NOT the line used to display the customer's 
                                               # profile. The '__str__' method is used below when print(account) is called.
    print(account) # 2b) Prints the argument value passed to object 'account' by the class 'BankAccount' (see right above!)

# ============ Transaction Scenarios ============
    # I) Demonstrates a successful deposit:
    try:
        account.deposit(100)
    except ValueError as e: 
        print(f"Error: {e}") 

    # II) Demonstrates a successful withdrawal:
    try:
        account.withdraw(50)
    except ValueError as e: 
        print(f"Error: {e}") 

    # III) Attempts a withdrawal that exceeds the current balance:
    try:
        account.withdraw(800)
    except ValueError as e: 
        print(f"Error: {e}") 

    # IV) Attempts a withdrawal using a negative amount:
    try:
        account.withdraw(-1)
    except ValueError as e: 
        print(f"Error: {e}") 

    # V) Attempts a deposit using a negative amount:
    try:
        account.deposit(-10)
    except ValueError as e: 
        print(f"Error: {e}") 

    print(account) # Displays the account's final balance after all transactions.
    
# This guard prevents Python from running main() when bank.py is imported into another file. 
# The BankAccount class remains available for importing.
if __name__ == "__main__": 
    main() 


















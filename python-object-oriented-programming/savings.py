''' 
Savings Account Management - Subclass
Demonstrates object-oriented programming (OOP) concepts by defining a SavingsAccount subclass that inherits from BankAccount.
Includes an additional interest_rate attribute, an initializer using super().__init__(), an apply_interest() method, 
and an overridden __str__() method.
Includes test code demonstrating inherited deposit and withdrawal functionalities, interest application, and exception handling.
'''

from bank import BankAccount # importing the SUPERCLASS 'BankAccount' from the file 'bank.py'

class SavingsAccount(BankAccount): # Declaring that SUBCLASS 'SavingsAccount' inherits from SUPERCLASS 'BankAccount'
                                   # In other words, 'SavingsAccount' is a child of 'BankAccount' and inherits its functionality.

    # Adds an Attribute and Modifies the Initializer:
    # Adds attribute 'interest_rate=0' and modifies the initializer to accept interest_rate along with other parameters and calls 
    # the base class initializer using 'super().__init__()'
    def __init__(self, account_number, owner, balance=0, interest_rate=0): # listing the additional attribute 'interest_rate', in 
                                                                           # addition to those being inherited from 'BankAccount'.
        super().__init__(account_number, owner, balance) # This subclass 'SavingsAccount' has to call 'super().__init__(...)', 
                                                         # so the parent’s setup (account_number, owner, balance) still runs 
                                                         # before adding the 'interest_rate' attribute here in the subclass.
                                                         # 'super()' is a built-in function that returns a proxy object,
                                                         # allowing you to call methods from the parent class (or next
                                                         # class in the method resolution order, MRO)..
                                                         # * Passes the 3 shared values up to BankAccount.__init__(), which  
                                                         # initializes self.account_number, self.owner, and self.balance.
        self.interest_rate = interest_rate # This line stores the additional attribute 'interest_rate', directly on the
                                           # SavingsAccount instance.
                                           # Note that 'interest_rate' is not passed to 'super().__init__()', because BankAccount 
                                           # doesn’t know about this additional attribute .

    # Additional Method:
    # apply_interest(self): Calculates the interest based on the current balance and interest_rate, then adds it to the balance. 
    # For example, if the interest rate is 5%, it adds balance * 0.05 to the balance:
    def apply_interest(self):
        # Calculates the interest using the savings account's interest rate and current balance:

        # interest = (interest_rate / 100) * 1) self.balance # 'interest_rate' by itself will not work here to calculate 'interest'.
        interest = (self.interest_rate / 100) * self.balance # 2) 'self.interest_rate' will work bc it specificies that it
                                                              # is not just interest rate that we want, but rather 
                                                              # the 'interest rate for the SAVINGS ACCOUNT' to calc the interest.
        self.balance += interest # Updates the account balance by adding the calculated interest.
                                 # This changes the balance stored on this SavingsAccount instance.
        # print(f"Interest Applied: {interest_rate}") # 3) again, this line references some 'interest_rate', so it will not work
        print(f"Interest rate applied: {self.interest_rate}%") # 4) rather, 'self.interest_rate' specificies that it is the 'interest rate
                                                             # for the SAVINGS ACCOUNT' that we want print. In other words, it displays the 
                                                             # interest rate stored on this SavingsAccount instance and used in the 
                                                             # interest calculation.                                                                                  
        print(f"Interest earned: ${interest:.2f}")  # 5) It displays the interest earned, formatted to two decimal places.
        print(f"New balance: ${self.balance:.2f}")  # 6)'self.balance' specificies that it is the 'balance for the SAVINGS ACCOUNT'
                                                    # that we want print and NOT the balance for 'BankAccount' in file 'bank.py'.
                                                    # In other words, it displays the updated balance of this SavingsAccount object.
                                                    # This is the inherited 'balance' attribute, originally initialized
                                                    # by BankAccount.__init__().
 
    # Method Overriding:
    # Overrides BankAccount.__str__() to include the savings account's interest rate in its string representation.
    def __str__(self):                     
        return f"{super().__str__()}, Interest Rate: {self.interest_rate}%" 


if __name__ == "__main__": # This guard runs the indented test code only when savings.py is run directly. 
                           # If another file imports savings.py, this block is skipped, but the
                           # SavingsAccount class remains available for importing.

# ============ Savings Account Scenarios ============

    savings = SavingsAccount(989998, "Bob", 500, 15) # Creating the object 'savings' which is an instance of class 'SavingsAccount'.  
    print(savings)             # Printing the contents/values of the 'savings' object, BEFORE interest being applied. 
    savings.apply_interest()   # Applying the method 'apply_interest()' to the 'savings' object: 15% of 500 = 75
    print(savings)             # Printing the contents/values of the 'savings' object AFTER interest is applied., in which only
                               # the 'balance' attribute is modified by calling 'apply_interest()'.
                               # The 'interest_rate' attribute remains unchanged.

    # Demonstrates the inherited deposit and withdraw functionality:
    # I) Inherited 'deposit' functionality:
    try:
        savings.deposit(100)
    except ValueError as e:
        print(f"Error: {e}")

    # II) Inherited 'withdraw' functionality.
    try:
        savings.withdraw(10)
    except ValueError as e:
        print(f"Error: {e}")

    # III) Exception handling when attempting to withdraw more than the current balance.
    try:
        savings.withdraw(1000)
    except ValueError as e:
        print(f"Error: {e}")

    # IV) Exception handling when attempting to deposit a negative amount.
    try:
        savings.deposit(-1)
    except ValueError as e:
        print(f"Error: {e}")

    # V) Exception handling when attempting to withdraw a negative amount.
    try:
        savings.withdraw(-1)
    except ValueError as e:
        print(f"Error: {e}")

    # Displays the account's final balance after all transactions.
    print(savings)













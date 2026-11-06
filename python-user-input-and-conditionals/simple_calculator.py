print()

# A 'simple_calculator.py' Python script:

num1 = input("Please enter the first number: ") # takes 1st input, no casting input to integer here.
num2 = input("Please enter the second number: ")  # takes 2nd input, no casting input to integer here. 

## Asks the user to choose an operation (e.g., (+, -, *, /)):
operator = input("Please choose operator: ") # allows you to select the operator.

## Performs the chosen operation on the two numbers:
if not num1.isdigit() or not num2.isdigit(): # this code line implements 'isdigit()' that checks whether the string contains only
                                             # digit characters, so it accepts non-negative whole numbers only. -5 fails even 
                                             # though it’s an integer.
    print("Please enter a valid input!") # this says that if either of the above 2 conditions is True, the input is invalid and 
                                         # this message gets printed.
else: 
    num1 = int(num1) # ...otherwise, it casts input to integer
    num2 = int(num2) # ...and same here, casts input to integer

    if operator == '+': # if operator is addition, then...
        total = num1 + num2 # this line now performs the addition and uses 'total' instead of 'sum' as the storage variable.
        print(f"{num1} + {num2} = {total}") # and prints the result in a user-friendly way. Note changed 'sum' var to 'total' var
    elif operator == '-': # else if operator is subtraction, then...
        difference = num1 - num2 # this line runs and performs subtraction.
        print(f"{num1} - {num2} = {difference}") # and prints the result in a user-friendly way
    elif operator == '*':  # else if operator is multiplication, then...
        product = num1 * num2 # this line runs and performs multiplication.
        print(f"{num1} * {num2} = {product}") # and prints the result in a user-friendly way
    elif operator == '/': # else if operator is division, AND...
        if num2 == 0:  #...if the divisor is zero, then...
            print("Cannot divide by zero!") # it prints this message
        else: # otherwise within the division conditional branch still...
            quotient = num1 / num2  # this line runs and performs division.
            print(f"{num1} / {num2} = {quotient}") # and prints the result in a user-friendly way.
    else:
        print("Please enter a valid operator!") # otherwise, it's not a valid operator after all.
print() 


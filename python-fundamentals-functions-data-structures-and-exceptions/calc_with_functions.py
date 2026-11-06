"""Calculator with functions.
Refactors the simple calculator into functions. add(), subtract(), multiply(), and divide() each do one operation and return 
the result, and calculate() uses if/elif to pick the right one for a given operator symbol. The main program asks for two numbers and an operator, then prints the result.
Invalid numeric input is caught with try/except in the main program, and division by zero is caught inside divide().

Note: divide() and calculate() return error messages as strings instead of raising exceptions, so the main program can simply 
print whatever comes back.
"""

# =============================== LOGIC ================================================== #
# add(a,b), subtract(a,b), multiply(a,b), divide(a,b) – each returning the result.

## Description: these are four individual functions that handle each of the 4 types of operations (+, -, *, /):
def add(a, b): # 'a' and 'b' are the two numbers to add
    return a + b  #returns their sum

def subtract(a,b): # 'a' is the number to subtract from; 'b' is the number to subtract
    return a - b # returns the difference

def multiply(a,b): # 'a' and 'b' are the two numbers to multiply
    return a * b # returns their product

def divide(a,b):  #  'a' is the number to be divided (numerator); 'b' is the number to divide by (denominator)
    try:
        return a / b # returns the quotient, or an error message if b is 0
    except ZeroDivisionError: # catches division by zero and returns a friendly message instead of crashing
        return "Error: cannot divide by zero!"
# Encapsulated the expression 'return a / b' within a 'try/except' block, so that if a number is ever divided by zero, rather than
# displaying a highly technical message for the user to figure out, this block catches the error and returns the exception in
# a much more simplified exception message, in this case "Error: cannot divide by zero!"


# calculate(a, b, op) takes two numbers and operation symbol, and uses if/elif to call the correct operation function. 
# It handles an invalid operation by returning an error message.

## Description: this function applies/executes any of the above functions on 2 given operands, depending on the operation symbol entered!
def calculate(a, b, op): # 'a' and 'b' are the numbers; 'op' is the symbol (+, -, *, /)
    if op == "+":
        # add = a + b
        # add(a, b)
        return add(a, b) # returns the sum total of 2 numbers, by calling the function 'add(a, b)' onto them.
    elif op == "-":
        # minus = a - b
        # subtract(a,b)
        return subtract(a,b) # returns the difference between 2 numbers, by calling the function 'subtract(a, b)' onto them.
    elif op == "*":
        # times = a * b
        # multiply(a,b)
        return multiply(a,b)  # returns the product of 2 numbers, by calling the function 'multiply(a, b)' onto them.
    elif op == "/":
        # divide = a / b
        # divide(a,b)
        return divide(a,b)  # returns the quotient of 2 numbers, by calling the function 'divide(a, b)' onto them.
    else:
        return "Invalid operation. Try again!" # returns (not prints) the message, so the main program prints it just once

# =============================== MAIN ================================================== #
# In the main program, it asks the user for 2 numbers and an operation (just like before), but now uses the calculate function 
# to get the result and print it.

## This is the main program, made up of... 
## 1) INPUT: 3 separate input functions, 2 for each number entered and the one in the middle for the operation of choice.
## 2) OUTPUT: the output made of... 
### the function call
### the result print

try:
    # INPUT:
    a = float(input("Enter first number: ")) # takes in the 1st number and stores it in 'a' variable
    op = input("Enter operation sign: ") # takes in the operation symbol
    b = float(input("Enter second number: ")) # takes in the 2nd number and stores it in 'b' variable
    # OUTPUT:
    result = calculate(a, b, op)  # a call to the function 'calculate' is made when the user enters values for each of 3 variables
    print(result) # then the result is printed
except ValueError:
    print("Invalid input. Please enter valid numbers.")  
# Encapsulated the main program within a 'try/except' block, so that if any input type other than 'float' is entered at the
# first input request, rather than displaying a highly technical message for the user to figure out, this block catches the 
# error and returns the exception in a much more simplified exception message in this case...
#  "Invalid input. Please enter valid numbers."
